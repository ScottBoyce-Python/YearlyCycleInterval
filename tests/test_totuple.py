from DateIntervalCycler import DateIntervalCycler
import datetime as dt
import pytest

ans_for_1_and_2 = tuple(
    dt.datetime.strptime(date, "%Y-%m-%d")
    for date in (
        "2000-02-01",  # Note, it honors the starting date
        "2000-04-01",  # Follows the month and day defined by "cycles"
        "2000-07-01",
        "2000-10-01",
        "2001-01-01",
        "2001-04-01",
        "2001-07-01",
        "2001-10-01",
        "2002-01-01",
        "2002-04-01",
        "2002-07-01",
        "2002-10-01",
        "2003-01-01",
        "2003-04-01",
        "2003-07-01",
        "2003-10-01",
        "2004-01-01",
        "2004-04-01",
        "2004-07-01",
        "2004-10-01",
        "2005-01-01",
        "2005-04-01",
        "2005-07-01",
        "2005-10-01",
        "2005-11-01",  # Note, it honors the ending date
    )
)

ans_for_3 = tuple(
    dt.datetime.strptime(date, "%Y-%m-%d")
    for date in (
        "1950-01-15",  # Note, it honors the starting date
        "1950-01-31",  # Follows the month and day defined by "cycles"
        "1950-02-28",
        "1950-03-31",
        "1950-04-30",
        "1950-05-31",
        "1950-06-30",
        "1950-07-31",
        "1950-08-31",
        "1950-09-30",
        "1950-10-31",
        "1950-11-30",
        "1950-12-31",
        "1951-01-31",
        "1951-02-28",
        "1951-03-31",
        "1951-04-30",
        "1951-05-31",
        "1951-06-30",
        "1951-07-31",
        "1951-08-31",
        "1951-09-30",
        "1951-10-31",
        "1951-11-30",
        "1951-12-31",
        "1952-01-31",
        "1952-02-29",
        "1952-03-31",
        "1952-04-30",
        "1952-05-31",
        "1952-06-30",
        "1952-07-31",
        "1952-08-31",
        "1952-09-30",
        "1952-10-31",
        "1952-11-30",
        "1952-12-31",
        "1953-01-31",
        "1953-02-28",
        "1953-03-31",
        "1953-04-30",
        "1953-05-31",
        "1953-06-30",
        "1953-07-31",
        "1953-08-31",
        "1953-09-30",
        "1953-10-31",
        "1953-11-30",
        "1953-12-31",
        "1954-01-31",
        "1954-02-28",
        "1954-03-31",
        "1954-04-30",
        "1954-05-31",
        "1954-06-30",
        "1954-07-31",
        "1954-08-31",
        "1954-09-30",
        "1954-10-31",
        "1954-11-30",
        "1954-12-31",
        "1955-01-31",
        "1955-02-28",
        "1955-03-31",
        "1955-04-30",
        "1955-05-31",
        "1955-06-30",
        "1955-07-31",
        "1955-08-31",
        "1955-09-30",
        "1955-10-31",
        "1955-11-30",
        "1955-12-31",
        "1956-01-31",
        "1956-02-29",
        "1956-03-31",
        "1956-04-30",
        "1956-05-31",
        "1956-06-30",
        "1956-07-31",
        "1956-08-31",
        "1956-09-30",
        "1956-10-31",
        "1956-11-30",
        "1956-12-31",
        "1957-01-31",
        "1957-02-28",
        "1957-03-31",
        "1957-04-30",
        "1957-05-31",
        "1957-06-30",
        "1957-07-31",
        "1957-08-31",
        "1957-09-30",
        "1957-10-31",
        "1957-11-30",
        "1957-12-31",
        "1958-01-31",
        "1958-02-28",
        "1958-03-31",
        "1958-04-30",
        "1958-05-31",
        "1958-06-30",
        "1958-07-31",
        "1958-08-31",
        "1958-09-30",
        "1958-10-31",
        "1958-11-30",
        "1958-12-31",
        "1959-01-31",
        "1959-02-28",
        "1959-03-31",
        "1959-04-30",
        "1959-05-31",
        "1959-06-30",
        "1959-07-31",
        "1959-08-31",
        "1959-09-30",
        "1959-10-31",
        "1959-11-30",
        "1959-12-31",
        "1960-01-31",
        "1960-02-29",
        "1960-03-31",
        "1960-04-30",
        "1960-05-31",
        "1960-06-30",
        "1960-07-31",
        "1960-08-31",
        "1960-09-30",
        "1960-10-31",
        "1960-11-30",
        "1960-12-31",
        "1961-01-31",
        "1961-02-28",
        "1961-03-31",
        "1961-04-30",
        "1961-05-31",
        "1961-06-30",
        "1961-07-31",
        "1961-08-31",
        "1961-09-30",
        "1961-10-31",
        "1961-11-30",
        "1961-12-31",
        "1962-01-31",
        "1962-02-28",
        "1962-03-31",
        "1962-04-30",
        "1962-05-31",
        "1962-06-30",
        "1962-07-31",
        "1962-08-31",
        "1962-09-30",
        "1962-10-31",
        "1962-11-30",
        "1962-12-31",
        "1963-01-31",
        "1963-02-28",
        "1963-03-31",
        "1963-04-30",
        "1963-05-31",
        "1963-06-30",
        "1963-07-31",
        "1963-08-31",
        "1963-09-30",
        "1963-10-31",
        "1963-11-30",
        "1963-12-31",
        "1964-01-31",
        "1964-02-29",
        "1964-03-31",
        "1964-04-30",
        "1964-05-31",
        "1964-06-30",
        "1964-07-31",
        "1964-08-31",
        "1964-09-30",
        "1964-10-31",
        "1964-11-30",
        "1964-12-31",
        "1965-01-31",
        "1965-02-28",
        "1965-03-31",
        "1965-04-30",
        "1965-05-31",
        "1965-06-30",
        "1965-07-31",
        "1965-08-31",
        "1965-09-30",
        "1965-10-31",
        "1965-11-30",
        "1965-12-31",
        "1966-01-31",
        "1966-02-28",
        "1966-03-31",
        "1966-04-30",
        "1966-05-31",
        "1966-06-30",
        "1966-07-31",
        "1966-08-31",
        "1966-09-30",
        "1966-10-31",
        "1966-11-30",
        "1966-12-31",
        "1967-01-31",
        "1967-02-28",
        "1967-03-31",
        "1967-04-30",
        "1967-05-31",
        "1967-06-30",
        "1967-07-31",
        "1967-08-31",
        "1967-09-30",
        "1967-10-31",
        "1967-11-30",
        "1967-12-31",
        "1968-01-31",
        "1968-02-29",
        "1968-03-31",
        "1968-04-30",
        "1968-05-31",
        "1968-06-30",
        "1968-07-31",
        "1968-08-31",
        "1968-09-30",
        "1968-10-31",
        "1968-11-30",
        "1968-12-31",
        "1969-01-31",
        "1969-02-28",
        "1969-03-31",
        "1969-04-30",
        "1969-05-31",
        "1969-06-30",
        "1969-07-31",
        "1969-08-31",
        "1969-09-30",
        "1969-10-31",
        "1969-11-30",
        "1969-12-31",
        "1970-01-31",
        "1970-02-28",
        "1970-03-31",
        "1970-04-30",
        "1970-05-31",
        "1970-06-30",
        "1970-07-31",
        "1970-08-31",
        "1970-09-30",
        "1970-10-31",
        "1970-11-30",
        "1970-12-31",
        "1971-01-31",
        "1971-02-28",
        "1971-03-31",
        "1971-04-30",
        "1971-05-31",
        "1971-06-30",
        "1971-07-31",
        "1971-08-31",
        "1971-09-30",
        "1971-10-31",
        "1971-11-30",
        "1971-12-31",
        "1972-01-31",
        "1972-02-29",
        "1972-03-31",
        "1972-04-30",
        "1972-05-31",
        "1972-06-30",
        "1972-07-31",
        "1972-08-31",
        "1972-09-30",
        "1972-10-31",
        "1972-11-30",
        "1972-12-31",
        "1973-01-31",
        "1973-02-28",
        "1973-03-31",
        "1973-04-30",
        "1973-05-31",
        "1973-06-30",
        "1973-07-31",
        "1973-08-31",
        "1973-09-30",
        "1973-10-31",
        "1973-11-30",
        "1973-12-31",
        "1974-01-31",
        "1974-02-28",
        "1974-03-31",
        "1974-04-30",
        "1974-05-31",
        "1974-06-30",
        "1974-07-31",
        "1974-08-31",
        "1974-09-30",
        "1974-10-31",
        "1974-11-30",
        "1974-12-31",
        "1975-01-31",
        "1975-02-28",
        "1975-03-31",
        "1975-04-30",
        "1975-05-31",
        "1975-06-30",
        "1975-07-31",
        "1975-08-31",
        "1975-09-30",
        "1975-10-31",
        "1975-11-30",
        "1975-12-31",
        "1976-01-31",
        "1976-02-29",
        "1976-03-31",
        "1976-04-30",
        "1976-05-31",
        "1976-06-30",
        "1976-07-31",
        "1976-08-31",
        "1976-09-30",
        "1976-10-31",
        "1976-11-30",
        "1976-12-31",
        "1977-01-31",
        "1977-02-28",
        "1977-03-31",
        "1977-04-30",
        "1977-05-31",
        "1977-06-30",
        "1977-07-31",
        "1977-08-31",
        "1977-09-30",
        "1977-10-31",
        "1977-11-30",
        "1977-12-31",
        "1978-01-31",
        "1978-02-28",
        "1978-03-31",
        "1978-04-30",
        "1978-05-31",
        "1978-06-30",
        "1978-07-31",
        "1978-08-31",
        "1978-09-30",
        "1978-10-31",
        "1978-11-30",
        "1978-12-31",
        "1979-01-31",
        "1979-02-28",
        "1979-03-31",
        "1979-04-30",
        "1979-05-31",
        "1979-06-30",
        "1979-07-31",
        "1979-08-31",
        "1979-09-30",
        "1979-10-31",
        "1979-11-30",
        "1979-12-31",
        "1980-01-31",
        "1980-02-12",  # Note, it honors the ending date
    )
)


def test_totuple_value_error():
    cid = DateIntervalCycler.with_monthly(dt.datetime(1950, 1, 1))

    with pytest.raises(ValueError):  # missing end date
        cid.totuple()


def test_totuple1():
    cycles = [
        (1, 1),  # (month, day)
        (4, 1),
        (7, 1),
        (10, 1),
    ]

    cid = DateIntervalCycler(cycles, dt.datetime(1950, 1, 1))

    start = dt.datetime(2000, 2, 1)
    end = dt.datetime(2005, 11, 1)  # note totuple is is inclusive for end date

    assert cid.totuple(start, end) == ans_for_1_and_2

    cid = DateIntervalCycler(cycles, start, end, start_before_first_interval=True)

    assert cid.totuple() == ans_for_1_and_2


def test_totuple2():
    cycles = [
        (1, 1),  # (month, day)
        (4, 1),
        (7, 1),
        (10, 1),
    ]

    cid = DateIntervalCycler(cycles, dt.datetime(2000, 2, 1))

    assert cid.totuple(3, 10) == ans_for_1_and_2[3 : 10 + 1]  # note list includes extra for end date

    cid = DateIntervalCycler(cycles, dt.datetime(2000, 2, 1), start_before_first_interval=True)

    assert cid.totuple(3, 10) == ans_for_1_and_2[3 : 10 + 1]


def test_totuple3():
    cid = DateIntervalCycler.with_monthly_end(dt.datetime(1950, 1, 15), dt.datetime(1980, 2, 12))

    assert cid.totuple() == ans_for_3

    cid = DateIntervalCycler.with_monthly_end(
        dt.datetime(1950, 1, 15),
        dt.datetime(1980, 2, 12),
        start_before_first_interval=True,
    )

    assert cid.totuple() == ans_for_3


@pytest.mark.parametrize(
    "end_date",
    [
        end_date
        for end_date in [
            dt.datetime(1953, 2, 5),
            dt.datetime(1953, 2, 28),
            dt.datetime(1953, 3, 12),
            dt.datetime(1956, 2, 5),
            dt.datetime(1956, 2, 29),
            dt.datetime(1956, 3, 12),
            dt.datetime(1967, 3, 12),
            dt.datetime(1968, 3, 12),
        ]
    ],
)
def test_totuple3_index(end_date: dt.datetime):
    cid = DateIntervalCycler.with_monthly_end(dt.datetime(1950, 1, 15), end_date)
    ans = ans_for_3[: cid.size] + (end_date,)
    dim = len(ans)
    for i in range(dim):
        it = 0 if i < 3 else i - 2
        for j in range(it, dim):
            if i < j:
                assert cid.totuple(i, j) == ans[i : j + 1]
            else:
                assert cid.totuple(i, j) == ()


def test_totuple_single_cycle():
    cycles = [
        (6, 1),  # Duplicate should be dropped
    ]

    cid = DateIntervalCycler(cycles, dt.datetime(2000, 3, 1), dt.datetime(2019, 7, 1))
    ans = tuple(
        dt.datetime.strptime(date, "%Y-%m-%d")
        for date in (
            "2000-3-1",  # Note, it honors the starting date
            "2000-6-1",  # Follows the month and day defined by "cycles"
            "2001-6-1",
            "2002-6-1",
            "2003-6-1",
            "2004-6-1",
            "2005-6-1",
            "2006-6-1",
            "2007-6-1",
            "2008-6-1",
            "2009-6-1",
            "2010-6-1",
            "2011-6-1",
            "2012-6-1",
            "2013-6-1",
            "2014-6-1",
            "2015-6-1",
            "2016-6-1",
            "2017-6-1",
            "2018-6-1",
            "2019-6-1",
            "2019-7-1",  # Note, it honors the ending date
        )
    )
    lst = cid.totuple()
    assert lst == ans

    dim = len(ans)
    for i in range(dim):
        it = 0 if i < 3 else i - 2
        for j in range(it, dim):
            if i < j:
                assert cid.totuple(i, j) == ans[i : j + 1]
            else:
                assert cid.totuple(i, j) == ()


y0 = 2000  # Must be leap year
yN = 2004  # Must be leap year

start_lists = (
    [dt.datetime(y0, m, 1) for m in range(1, 13)],
    [dt.datetime(y0, m, 5) for m in range(1, 13)],
    [dt.datetime(y0 - 1, m, 1) for m in range(1, 13)],
    [dt.datetime(y0 - 1, m, 5) for m in range(1, 13)],
    [dt.datetime(y0 + 1, m, 1) for m in range(1, 13)],
    [dt.datetime(y0 + 1, m, 5) for m in range(1, 13)],
    [dt.datetime(y0, m, DateIntervalCycler.MONTH_DAYS_LEAP[m]) for m in range(1, 13)],
    [dt.datetime(y0 - 1, m, (0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31)[m]) for m in range(1, 13)],
    [dt.datetime(y0 + 1, m, (0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31)[m]) for m in range(1, 13)],
    [
        dt.datetime(y0, 2, 28),
        dt.datetime(y0, 2, 29),
        dt.datetime(y0, 3, 1),
        dt.datetime(y0 + 1, 2, 28),
        dt.datetime(y0 + 1, 3, 1),
    ],
)

end_list = (
    [dt.datetime(yN, m, 1) for m in range(1, 13)]
    + [dt.datetime(yN, m, 5) for m in range(1, 13)]
    + [dt.datetime(yN - 1, m, 1) for m in range(1, 13)]
    + [dt.datetime(yN - 1, m, 5) for m in range(1, 13)]
    + [dt.datetime(yN + 1, m, 1) for m in range(1, 13)]
    + [dt.datetime(yN + 1, m, 5) for m in range(1, 13)]
    + [dt.datetime(yN, m, DateIntervalCycler.MONTH_DAYS_LEAP[m]) for m in range(1, 13)]
    + [dt.datetime(yN - 1, m, (0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31)[m]) for m in range(1, 13)]
    + [dt.datetime(yN + 1, m, (0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31)[m]) for m in range(1, 13)]
    + [
        dt.datetime(yN, 2, 28),
        dt.datetime(yN, 2, 29),
        dt.datetime(yN, 3, 1),
        dt.datetime(yN + 1, 2, 28),
        dt.datetime(yN + 1, 3, 1),
    ]
)


@pytest.mark.parametrize("start_list, end_list", [(start_list, end_list) for start_list in start_lists])
def test_totuple_tolist(start_list, end_list):
    for start in start_list:
        for end in end_list:
            cid = DateIntervalCycler.with_daily(start, end)
            assert cid.totuple() == tuple(cid.tolist(only_start=True)) + (cid.last_interval_end,)

            cid = DateIntervalCycler.with_monthly(start, end)
            assert cid.totuple() == tuple(cid.tolist(only_start=True)) + (cid.last_interval_end,)

            cid = DateIntervalCycler.with_monthly_end(start, end)
            assert cid.totuple() == tuple(cid.tolist(only_start=True)) + (cid.last_interval_end,)
