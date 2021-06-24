import React from 'react';
import DateRangePicker from 'react-bootstrap-daterangepicker';
import Chart from './Chart';
import SymbolInput from './SymbolInput';


function App() {
  return (
    <div className="container">
      <h1 style={{ marginBottom: "24px" }}>Stocks Search</h1>
      <div style={{ float: "left", width: "50%" }}>
        <SymbolInput />
      </div>
      <div style={{ float: "left", width: "50%" }}>
        <DateRangePicker>
          <input type="text" className="form-control" />
        </DateRangePicker>
      </div>
      <div style={{ clear: "both" }}></div>
      <div style={{ marginTop: "24px" }}>
        <Chart />
      </div>
    </div>
  );
}

export default App;
