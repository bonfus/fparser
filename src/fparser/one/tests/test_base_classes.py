import logging
import fparser.readfortran
import fparser.one.parsefortran

def test_statement(monkeypatch):
    '''
    Tests the Statement class.

    Only exercises the logging functionality at the moment.
    '''
    reader = fparser.readfortran.FortranStringReader("dummy = 1")
    parser = fparser.one.parsefortran.FortranParser(reader)

    logger = logging.getLogger('fparser')
    log = fparser.tests.logging_utils.CaptureLoggingHandler()
    logger.addHandler(log)

    monkeypatch.setattr(fparser.one.base_classes.Statement,
                        'process_item', lambda x: None, raising=False)
    unit_under_test = fparser.one.base_classes.Statement(parser, None)

    unit_under_test.error('Scary biscuits')
    assert(log.messages == {'critical': [],
                            'debug':    [],
                            'error':    ['Scary biscuits'],
                            'info':     [],
                            'warning':  []})
