# /usr/bin/env python
# -*- coding: utf-8 -*-

"""Tests using as library"""

import pytest
from conftest import cd

from symbol_version import symbol_version


def test_unitialized_all_global_symbols():
    m = symbol_version.Map()

    expected = "Map not checked, run check()"
    symbols = None

    with pytest.raises(Exception) as e:
        symbols = m.all_global_symbols()
        assert expected in str(e.value)

    assert not symbols


def test_unitialized_guess_latest_release():
    m = symbol_version.Map()

    expected = "Map not checked, run check()"
    symbols = None

    with pytest.raises(Exception) as e:
        symbols = m.guess_latest_release()
        assert expected in str(e.value)

    assert not symbols


def test_unitialized_sort_releases_nice():
    m = symbol_version.Map()

    expected = "Map not checked, run check()"
    symbols = None

    with pytest.raises(Exception) as e:
        symbols = m.sort_releases_nice(None)
        assert expected in str(e.value)

    assert not symbols


def test_empty_map(datadir):
    m = symbol_version.Map()

    expected = "Empty map"

    with pytest.raises(Exception) as e:
        m.check()
        assert expected in str(e.value)

    with cd(datadir):
        m.read("base.map")

        m.check()

        out = str(m)

        with open("empty_map.stdout") as tcout:
            assert out == tcout.read()


def test_guess_name_without_version(datadir):

    m = symbol_version.Map()

    expected = "".join(["Insufficient information to guess the new release",
                        " name. Releases found do not have version",
                        " information or a valid library name. Please",
                        " provide the complete name of the release."])

    with cd(datadir):
        with pytest.raises(Exception) as e:
            m.read("without_version.map")
            m.guess_name(None, guess=True)

            assert expected in str(e.value)


def test_guess_name_without_prefix(datadir):

    m = symbol_version.Map()
    expected = "".join(["Insufficient information to guess the new release",
                        " name. Releases found do not have version",
                        " information or a valid library name. Please",
                        " provide the complete name of the release."])

    with cd(datadir):
        with pytest.raises(Exception) as e:
            m.read("without_prefix.map")
            m.guess_name(None, guess=True)

            assert expected in str(e.value)


def test_guess_name_without_similar_prefix(datadir):

    m = symbol_version.Map()

    with cd(datadir):
        m.read("without_similar_prefix.map")
        m.guess_name(None, guess=True)
