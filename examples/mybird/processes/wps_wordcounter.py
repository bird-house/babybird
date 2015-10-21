"""
Example for a WPS Process implemented with PyWPS.

http://pywps.wald.intevation.org/documentation/course/process/index.html
http://birdhouse.readthedocs.org/en/latest/dev_guide.html
"""

import os

from pywps.Process import WPSProcess

import logging
logger = logging.getLogger(__name__)

class WordCountProcess(WPSProcess):
    """
    Counts words in a given text ...
    """
    def __init__(self):
        WPSProcess.__init__(
            self,
            identifier="wordcount", 
            title="Word Counter",
            version = "1.0",
            metadata = [],
            abstract="Counts words in a given text ...",
            storeSupported = True,
            statusSupported = True,
            )

        self.text = self.addComplexInput(
            identifier = "text",
            title = "Text document",
            abstract = "URL of text document",
            minOccurs=1,
            maxOccurs=1,
            formats=[{"mimeType":"text/plain"}],
            maxmegabites=2,
            )
        
        self.output = self.addComplexOutput(
            identifier = "output",
            title = "Word count result",
            formats=[{"mimeType":"text/plain"}],
            asReference=True,
            )
                                           
    def execute(self):
        self.status.set(msg="Starting ...", percentDone=0, propagate=True)

        import re
        wordre = re.compile(r'\w+')

        def words(f):
            for line in f:
                for word in wordre.findall(line):
                    yield word

        text = self.text.getValue()
        logger.debug('input file = %s', text)
        with open(text, 'r') as fin:
            from collections import Counter
            counts = Counter(words(fin))
            sorted_counts = sorted([(v,k) for (k,v) in counts.items()], reverse=True)
            import tempfile
            (_, outfile) = tempfile.mkstemp(dir=os.path.abspath(os.curdir), suffix='.txt')
            with open(outfile, 'w') as fout:
                logger.info('writing to %s', outfile)
                fout.write( str(sorted_counts) )
                self.output.setValue( fout.name )

        self.status.set(msg="Done", percentDone=100, propagate=True)

