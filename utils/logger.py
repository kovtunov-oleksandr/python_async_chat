import logging
import sys

logging.basicConfig(stream=sys.stderr, level=logging.NOTSET,
                    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')

logger = logging.getLogger(__name__)
