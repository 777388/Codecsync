import _multibytecodec
try:
    if (_multibytecodec.MultibyteIncrementalDecoder | _multibytecodec.MultibyteIncrementalEncoder):
        _multibytecodec.MultibyteStreamReader = _multibytecodec.MultibyteStreamWriter
except:
    _multibytecodec.__create_codec