import streamlit as st

def sum_rates(start_month, start_year, end_month, end_year, rates):
    total_rate = 0
    for month, year, rate in rates:
        if (year > start_year or (year == start_year and month >= start_month)) and \
           (year < end_year or (year == end_year and month <= end_month)):
            total_rate += rate
    return total_rate

# Sample rate data (replace with your actual data)
rates_list = [(7,2002,170),
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
    st.title("Rate Calculator")

    # Input fields
    with st.form("my_form"):
        start_month = st.selectbox("Start Month", options=range(1, 13))
        start_year = st.selectbox("Start Year", options=range(2000, 2025))
        end_month = st.selectbox("End Month", options=range(1, 13))
        end_year = st.selectbox("End Year", options=range(2000, 2025))
        ips = st.number_input("Number of IPs")
        submitted = st.form_submit_button("Calculate")
        Statutory_inc=st.number_input("SI rate",options=range(2,50))

    if submitted:
        # Calculate total rate
        total_rate = sum_rates(start_month, start_year, end_month, end_year, rates_list)
        total_payable = total_rate * ips
        employee_share = total_payable / 6
        employer_share = total_payable - employee_share
        si=(Statutory_inc*total_payable)/100

        # Display results
        st.write("Total Rate:", total_payable)
        st.write("Employer Share:", employer_share)
        st.write("Employee Share:", employee_share)
        st.wriite("Si increase:",si)

if __name__ == "__main__":
    main()
