//Component to allow user to select start and end months
//I chose to use React-Datepicker to implement this functionality 
//(https://github.com/Hacker0x01/react-datepicker)

import { useState } from "react";
import DatePicker from "react-datepicker";

import "react-datepicker/dist/react-datepicker.css";

interface MonthSelectProps {
  set_range: (range: [string, string]) => void;
}

const MonthSelect = ({ set_range }: MonthSelectProps ) => {
  //Start and end date of selector
  const [startDate, setStartDate] = useState<Date | null>(
    new Date("2026/04/01")
  );
  const [endDate, setEndDate] = useState<Date | null>(
    new Date("2026/04/01")
  );

  //Format dates from date object to formatted string
  function fmt(d: Date) {
    console.log(`${d.getFullYear()}-${String(d.getMonth() + 1).padStart(2, '0')}-01`)
    return `${d.getFullYear()}-${String(d.getMonth() + 1).padStart(2, '0')}-01`;
  }
    

  //When the dates are changed in the selector, change dates also in App.tsx
  const handleChange = ([newStartDate, newEndDate]: [Date | null, Date | null]) => {
    setStartDate(newStartDate);
    setEndDate(newEndDate);
    if (newStartDate && newEndDate) {
      set_range([fmt(newStartDate), fmt(newEndDate)]);
    } 
  };

  return (
    <div className="monthSelect">
      <p>Select Date Range:</p>
      <DatePicker
        selected={startDate}
        onChange={handleChange}
        selectsRange
        startDate={startDate}
        endDate={endDate}
        dateFormat="MM/yyyy"
        showMonthYearPicker
        className="picker"
        minDate={new Date("2024-10-01")}
        maxDate={new Date("2026-04-01")}
      />
    </div>
  );
};

export default MonthSelect;