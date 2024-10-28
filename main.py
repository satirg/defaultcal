import streamlit as st

def sum_rates(start_month, start_year, end_month, end_year, rates):
    total_rate = 0
    for month, year, rate in rates:
        if (year > start_year or (year == start_year and month >= start_month)) and \
           (year < end_year or (year == end_year and month <= end_month)):
            total_rate += rate
    return total_rate

rates_list = [(7,1976,50),
(8,1976,50),
(9,1976,50),
(10,1976,50),
(11,1976,50),
(12,1976,50),
(1,1977,50),
(2,1977,50),
(3,1977,50),
(4,1977,50),
(5,1977,50),
(6,1977,50),
(7,1977,50),
(8,1977,50),
(9,1977,50),
(10,1977,50),
(11,1977,50),
(12,1977,50),
(1,1978,50),
(2,1978,50),
(3,1978,50),
(4,1978,50),
(5,1978,50),
(6,1978,50),
(7,1978,50),
(8,1978,50),
(9,1978,50),
(10,1978,50),
(11,1978,50),
(12,1978,50),
(1,1979,50),
(2,1979,50),
(3,1979,50),
(4,1979,50),
(5,1979,50),
(6,1979,50),
(7,1979,50),
(8,1979,50),
(9,1979,50),
(10,1979,50),
(11,1979,50),
(12,1979,50),
(1,1980,50),
(2,1980,50),
(3,1980,50),
(4,1980,50),
(5,1980,50),
(6,1980,50),
(7,1980,50),
(8,1980,50),
(9,1980,50),
(10,1980,50),
(11,1980,50),
(12,1980,50),
(1,1981,50),
(2,1981,50),
(3,1981,50),
(4,1981,50),
(5,1981,50),
(6,1981,50),
(7,1981,50),
(8,1981,50),
(9,1981,50),
(10,1981,50),
(11,1981,50),
(12,1981,50),
(1,1982,50),
(2,1982,50),
(3,1982,50),
(4,1982,50),
(5,1982,50),
(6,1982,50),
(7,1982,50),
(8,1982,50),
(9,1982,50),
(10,1982,50),
(11,1982,50),
(12,1982,50),
(1,1983,50),
(2,1983,50),
(3,1983,50),
(4,1983,50),
(5,1983,50),
(6,1983,50),
(7,1983,50),
(8,1983,50),
(9,1983,50),
(10,1983,50),
(11,1983,50),
(12,1983,50),
(1,1984,50),
(2,1984,50),
(3,1984,50),
(4,1984,50),
(5,1984,50),
(6,1984,50),
(7,1984,50),
(8,1984,50),
(9,1984,50),
(10,1984,50),
(11,1984,50),
(12,1984,50),
(1,1985,50),
(2,1985,50),
(3,1985,50),
(4,1985,50),
(5,1985,50),
(6,1985,50),
(7,1985,75),
(8,1985,75),
(9,1985,75),
(10,1985,75),
(11,1985,75),
(12,1985,75),
(1,1986,75),
(2,1986,75),
(3,1986,75),
(4,1986,75),
(5,1986,75),
(6,1986,75),
(7,1986,75),
(8,1986,75),
(9,1986,75),
(10,1986,75),
(11,1986,75),
(12,1986,75),
(1,1987,75),
(2,1987,75),
(3,1987,75),
(4,1987,75),
(5,1987,75),
(6,1987,75),
(7,1987,75),
(8,1987,75),
(9,1987,75),
(10,1987,75),
(11,1987,75),
(12,1987,75),
(1,1988,75),
(2,1988,75),
(3,1988,75),
(4,1988,75),
(5,1988,75),
(6,1988,75),
(7,1988,75),
(8,1988,75),
(9,1988,75),
(10,1988,75),
(11,1988,75),
(12,1988,75),
(1,1989,75),
(2,1989,75),
(3,1989,75),
(4,1989,75),
(5,1989,75),
(6,1989,75),
(7,1989,75),
(8,1989,75),
(9,1989,75),
(10,1989,75),
(11,1989,75),
(12,1989,75),
(1,1990,75),
(2,1990,75),
(3,1990,75),
(4,1990,75),
(5,1990,75),
(6,1990,75),
(7,1990,75),
(8,1990,75),
(9,1990,75),
(10,1990,75),
(11,1990,75),
(12,1990,75),
(1,1991,75),
(2,1991,75),
(3,1991,75),
(4,1991,75),
(5,1991,75),
(6,1991,75),
(7,1991,75),
(8,1991,75),
(9,1991,75),
(10,1991,75),
(11,1991,75),
(12,1991,75),
(1,1992,75),
(2,1992,75),
(3,1992,75),
(4,1992,75),
(5,1992,75),
(6,1992,75),
(7,1992,75),
(8,1992,75),
(9,1992,75),
(10,1992,75),
(11,1992,75),
(12,1992,75),
(1,1993,75),
(2,1993,75),
(3,1993,75),
(4,1993,75),
(5,1993,75),
(6,1993,75),
(7,1993,75),
(8,1993,75),
(9,1993,75),
(10,1993,150),
(11,1993,150),
(12,1993,150),
(1,1994,150),
(2,1994,150),
(3,1994,150),
(4,1994,150),
(5,1994,150),
(6,1994,150),
(7,1994,150),
(8,1994,150),
(9,1994,150),
(10,1994,150),
(11,1994,150),
(12,1994,150),
(1,1995,150),
(2,1995,150),
(3,1995,150),
(4,1995,150),
(5,1995,150),
(6,1995,150),
(7,1995,150),
(8,1995,150),
(9,1995,150),
(10,1995,150),
(11,1995,150),
(12,1995,150),
(1,1996,150),
(2,1996,150),
(3,1996,150),
(4,1996,150),
(5,1996,150),
(6,1996,150),
(7,1996,150),
(8,1996,150),
(9,1996,150),
(10,1996,150),
(11,1996,150),
(12,1996,150),
(1,1997,150),
(2,1997,150),
(3,1997,150),
(4,1997,150),
(5,1997,150),
(6,1997,150),
(7,1997,150),
(8,1997,150),
(9,1997,150),
(10,1997,150),
(11,1997,150),
(12,1997,150),
(1,1998,150),
(2,1998,150),
(3,1998,150),
(4,1998,150),
(5,1998,150),
(6,1998,150),
(7,1998,150),
(8,1998,150),
(9,1998,150),
(10,1998,150),
(11,1998,150),
(12,1998,150),
(1,1999,150),
(2,1999,150),
(3,1999,150),
(4,1999,150),
(5,1999,150),
(6,1999,150),
(7,1999,150),
(8,1999,150),
(9,1999,150),
(10,1999,150),
(11,1999,150),
(12,1999,150),
(1,2000,150),
(2,2000,150),
(3,2000,150),
(4,2000,150),
(5,2000,150),
(6,2000,150),
(7,2000,150),
(8,2000,150),
(9,2000,150),
(10,2000,150),
(11,2000,150),
(12,2000,150),
(1,2001,150),
(2,2001,150),
(3,2001,150),
(4,2001,150),
(5,2001,150),
(6,2001,150),
(7,2001,170),
(8,2001,170),
(9,2001,170),
(10,2001,170),
(11,2001,170),
(12,2001,170),
(1,2002,170),
(2,2002,170),
(3,2002,170),
(4,2002,170),
(5,2002,170),
(6,2002,170),
(7,2002,170),
(8,2002,170),
(9,2002,170),
(10,2002,170),
(11,2002,170),
(12,2002,170),
(1,2003,170),
(2,2003,170),
(3,2003,170),
(4,2003,170),
(5,2003,170),
(6,2003,170),
(7,2003,170),
(8,2003,170),
(9,2003,170),
(10,2003,170),
(11,2003,170),
(12,2003,170),
(1,2004,170),
(2,2004,170),
(3,2004,170),
(4,2004,170),
(5,2004,170),
(6,2004,170),
(7,2004,170),
(8,2004,170),
(9,2004,170),
(10,2004,170),
(11,2004,170),
(12,2004,170),
(1,2005,170),
(2,2005,170),
(3,2005,170),
(4,2005,170),
(5,2005,170),
(6,2005,170),
(7,2005,210),
(8,2005,210),
(9,2005,210),
(10,2005,210),
(11,2005,210),
(12,2005,210),
(1,2006,210),
(2,2006,210),
(3,2006,210),
(4,2006,210),
(5,2006,210),
(6,2006,210),
(7,2006,280),
(8,2006,280),
(9,2006,280),
(10,2006,280),
(11,2006,280),
(12,2006,280),
(1,2007,280),
(2,2007,280),
(3,2007,280),
(4,2007,280),
(5,2007,280),
(6,2007,280),
(7,2007,322),
(8,2007,322),
(9,2007,322),
(10,2007,322),
(11,2007,322),
(12,2007,322),
(1,2008,322),
(2,2008,322),
(3,2008,322),
(4,2008,322),
(5,2008,322),
(6,2008,322),
(7,2008,360),
(8,2008,360),
(9,2008,360),
(10,2008,360),
(11,2008,360),
(12,2008,360),
(1,2009,360),
(2,2009,360),
(3,2009,360),
(4,2009,360),
(5,2009,360),
(6,2009,360),
(7,2009,360),
(8,2009,360),
(9,2009,360),
(10,2009,360),
(11,2009,360),
(12,2009,360),
(1,2010,360),
(2,2010,360),
(3,2010,360),
(4,2010,360),
(5,2010,360),
(6,2010,360),
(7,2010,420),
(8,2010,420),
(9,2010,420),
(10,2010,420),
(11,2010,420),
(12,2010,420),
(1,2011,420),
(2,2011,420),
(3,2011,420),
(4,2011,420),
(5,2011,420),
(6,2011,420),
(7,2011,420),
(8,2011,420),
(9,2011,420),
(10,2011,420),
(11,2011,420),
(12,2011,420),
(1,2012,420),
(2,2012,420),
(3,2012,420),
(4,2012,420),
(5,2012,420),
(6,2012,420),
(7,2012,480),
(8,2012,480),
(9,2012,480),
(10,2012,480),
(11,2012,480),
(12,2012,480),
(1,2013,480),
(2,2013,480),
(3,2013,480),
(4,2013,480),
(5,2013,480),
(6,2013,480),
(7,2013,600),
(8,2013,600),
(9,2013,600),
(10,2013,600),
(11,2013,600),
(12,2013,600),
(1,2014,600),
(2,2014,600),
(3,2014,600),
(4,2014,600),
(5,2014,600),
(6,2014,600),
(7,2014,720),
(8,2014,720),
(9,2014,720),
(10,2014,720),
(11,2014,720),
(12,2014,720),
(1,2015,720),
(2,2015,720),
(3,2015,720),
(4,2015,720),
(5,2015,720),
(6,2015,720),
(7,2015,780),
(8,2015,780),
(9,2015,780),
(10,2015,780),
(11,2015,780),
(12,2015,780),
(1,2016,780),
(2,2016,780),
(3,2016,780),
(4,2016,780),
(5,2016,780),
(6,2016,780),
(7,2016,840),
(8,2016,840),
(9,2016,840),
(10,2016,840),
(11,2016,840),
(12,2016,840),
(1,2017,840),
(2,2017,840),
(3,2017,840),
(4,2017,840),
(5,2017,840),
(6,2017,840),
(7,2017,900),
(8,2017,900),
(9,2017,900),
(10,2017,900),
(11,2017,900),
(12,2017,900),
(1,2018,900),
(2,2018,900),
(3,2018,900),
(4,2018,900),
(5,2018,900),
(6,2018,900),
(7,2018,990),
(8,2018,990),
(9,2018,990),
(10,2018,990),
(11,2018,990),
(12,2018,990),
(1,2019,990),
(2,2019,990),
(3,2019,990),
(4,2019,990),
(5,2019,990),
(6,2019,990),
(7,2019,1050),
(8,2019,1050),
(9,2019,1050),
(10,2019,1050),
(11,2019,1050),
(12,2019,1050),
(1,2020,1050),
(2,2020,1050),
(3,2020,1050),
(4,2020,1050),
(5,2020,1050),
(6,2020,1050),
(7,2020,1050),
(8,2020,1050),
(9,2020,1050),
(10,2020,1050),
(11,2020,1050),
(12,2020,1050),
(1,2021,1050),
(2,2021,1050),
(3,2021,1050),
(4,2021,1050),
(5,2021,1050),
(6,2021,1050),
(7,2021,1200),
(8,2021,1200),
(9,2021,1200),
(10,2021,1200),
(11,2021,1200),
(12,2021,1200),
(1,2022,1200),
(2,2022,1200),
(3,2022,1200),
(4,2022,1500),
(5,2022,1500),
(6,2022,1500),
(7,2022,1500),
(8,2022,1500),
(9,2022,1500),
(10,2022,1500),
(11,2022,1500),
(12,2022,1500),
(1,2023,1500),
(2,2023,1500),
(3,2023,1500),
(4,2023,1500),
(5,2023,1500),
(6,2023,1500),
(7,2023,1920),
(8,2023,1920),
(9,2023,1920),
(10,2023,1920),
(11,2023,1920),
(12,2023,1920),
(1,2024,1920),
(2,2024,1920),
(3,2024,1920),
(4,2024,1920),
(5,2024,1920),
(6,2024,1920),
(7,2024,2220),
(8,2024,2220),
(9,2024,2220),
(10,2024,2220),
(11,2024,2220),
(12,2024,2220),
]


def main():
    st.title("Rate Calculator ")
    st.title("Developed By S.A.G ")

    # Input fields
    with st.form("my_form"):
        start_month = st.selectbox("Start Month", options=range(1, 13))
        start_year = st.selectbox("Start Year", options=range(2002, 2025))
        end_month = st.selectbox("End Month", options=range(1, 13))
        end_year = st.selectbox("End Year", options=range(2002, 2025))
        ips = st.number_input("Number of IPs",format="%d")
        Statutory_inc=st.selectbox("SI rate",options=range(2,52,2))
        submitted = st.form_submit_button("Calculate")
        

    if submitted:
        # Calculate total rate
        total_rate = sum_rates(start_month, start_year, end_month, end_year, rates_list)
        total_payable = total_rate * ips
        employee_share = round(total_payable / 6)
        employer_share = total_payable - employee_share
        si=round((Statutory_inc*total_payable)/100)
        total_incsi=total_payable+si

        st.header("RESULTS ")
        st.write("Total Payable excluding SI:", total_payable)
        st.write("Total Payable Including SI:", total_incsi)
        st.write("Employer Share:", employer_share)
        st.write("Employee Share:", employee_share)
        st.write("Si increase:",si)
        



if __name__ == "__main__":
    main()
