import logging

stream_logger = logging.getLogger("stream_logger")
stream_logger.setLevel(logging.DEBUG)

stream_logger.handlers = []
stream_handler = logging.StreamHandler()
stream_handler.setLevel(logging.INFO)

stream_logger.addHandler(stream_handler)

stream_logger.debug("This is a debug message for stream logger.")
stream_logger.info("This is an info message for stream logger.")
stream_logger.warning("This is a warning message for stream logger.")
stream_logger.error("This is an error message for stream logger.")
stream_logger.critical("This is a critical message for stream logger.")

# different types of logging handlers
# logging.FileHandler
# logging.NullHandler
# logging.WatchedFileHandler
# logging.BaseRotatingHandler
# logging.RotatingFileHandler
# logging.TimedRotatingFileHandler

# logging.SocketHandler
# logging.DatagramHandler
# logging.SysLogHandler
# logging.NTEventLogHandler
# logging.SMTPHandler
# logging.MemoryHandler
# logging.HTTPHandler
# logging.QueueHandler
# logging.QueueListener
