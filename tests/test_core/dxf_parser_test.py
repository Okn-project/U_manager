from src.core.parsers.dxf_parser import DxfParser
import pytest
import os

SMALL_TEST_PATH = r"../data/small_test.dxf"
BIG_TEST_PATH = r"../data/big_test.dxf"
BAD_FILE_PATH = r"../data/bad_file.dxf"
NO_PATH = r""
WRONG_PATH = r"../data/WRONG_PATH.dxf"
NOT_DXF_PATH = r"../data/test_small.dwg"


def test_dxf_parser_reads_small_file():
    parser = DxfParser(SMALL_TEST_PATH)
    assert parser is not None
    parser.read_dxf()
    assert parser.doc is not None


def test_dxf_parser_reads_no_path():
    parser = DxfParser(NO_PATH)
    assert parser is not None
    with pytest.raises(FileNotFoundError):
        parser.read_dxf()


def test_dxf_parser_reads_wrong_path():
    parser = DxfParser(WRONG_PATH)
    assert parser is not None
    with pytest.raises(FileNotFoundError):
        parser.read_dxf()


def test_dxf_parser_reads_not_dxf_file():
    parser = DxfParser(NOT_DXF_PATH)
    assert parser is not None
    with pytest.raises(IOError):
        parser.read_dxf()


def test_dxf_parser_reads_bad_dxf_file():
    parser = DxfParser(BAD_FILE_PATH)
    assert parser is not None
    with pytest.raises(IOError):
        parser.read_dxf()
