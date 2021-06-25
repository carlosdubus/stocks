import React, { useState } from 'react';
import DateRangePicker from 'react-bootstrap-daterangepicker';
import Chart from './Chart';
import SymbolInput from './SymbolInput';
import * as moment from "moment";


function App() {
  const [startDate, setStartDate] = useState(moment().subtract(30, 'days'));
  const [endDate, setEndDate] = useState(moment().subtract(1, 'days'));
  const [symbol, setSymbol] = useState(null);
  const onDateChanged = (start, end) => {
    setStartDate(start);
    setEndDate(end);
  };
  const onSymbolChanged = (selected) => {
    if (selected && selected[0]) {
      setSymbol(selected[0]);
    }
  };
  return (
    <div className="container">
      <h1 style={{ marginBottom: "24px" }}>Stocks Search</h1>
      <div style={{ float: "left", width: "50%" }}>
        <SymbolInput onChange={onSymbolChanged} />
      </div>
      <div style={{ float: "left", width: "50%" }}>
        <DateRangePicker onCallback={onDateChanged} initialSettings={{
          startDate, endDate
        }}>
          <input type="text" className="form-control" />
        </DateRangePicker>
      </div>
      <div style={{ clear: "both" }}></div>
      <div style={{ marginTop: "24px" }}>
        <Chart
          symbol={symbol}
          startDate={startDate.format("YYYY-MM-DD")}
          endDate={endDate.format("YYYY-MM-DD")}
        />
      </div>
    </div>
  );
}

export default App;
