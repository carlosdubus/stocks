import ApexChart from "react-apexcharts";
import React, { Component } from 'react';

class Chart extends Component {
    state = {
        hasData: false,
        loading: false,
        series: [{
            data: []
        }],
        options: {
            chart: {
                type: 'candlestick',
                height: 350
            },
            xaxis: {
                type: 'datetime'
            },
            yaxis: {
                tooltip: {
                    enabled: true
                }
            }
        },
    }
    constructor(props) {
        super(props);
        this.fetchData()
            .then(data => {
                this.setState({
                    ...this.state,
                    series: [{
                        data
                    }]
                });
            });
    }

    fetchData() {
        return fetch(`/api/stocks?symbol=ASAL`)
            .then((resp) => resp.json())
            .then(stocks => {
                return stocks.map(row => ({
                    x: new Date(row.date),
                    y: [
                        parseFloat(row.price_open),
                        parseFloat(row.price_high),
                        parseFloat(row.price_low),
                        parseFloat(row.price_close)
                    ]
                }));
            });
    }

    render() {
        if (this.state.loading) {
            return <div className="text-center">
                <div className="spinner-grow" role="status">
                    <span className="sr-only">Loading...</span>
                </div>
            </div>
        }
        if (this.state.hasData) {
            return <ApexChart options={this.state.options} series={this.state.series} type="candlestick" height={350} />;
        }
        return <div></div>;
    }
}
export default Chart;