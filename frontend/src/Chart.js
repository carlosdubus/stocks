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

    componentDidMount() {
        this.fetchData()
    }

    componentDidUpdate(prevProps) {
        if (this.props.symbol != prevProps.symbol ||
            this.props.startDate != prevProps.startDate ||
            this.props.endDate != prevProps.endDate) {
            this.fetchData();
        }
    }

    fetchData() {
        if (!this.props.symbol || !this.props.startDate || !this.props.endDate) {
            this.setState({
                loading: false,
                hasData: false
            });
            return;
        }
        this.setState({
            loading: true
        });
        return fetch(`/api/stocks?symbol=${this.props.symbol}&from=${this.props.startDate}&to=${this.props.endDate}`)
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
            }).then(data => {
                this.setState({
                    loading: false,
                    hasData: data.length > 0,
                    series: [{
                        data
                    }],
                    options: {
                        ...this.state.options,
                        title: {
                            text: this.props.symbol,
                            align: 'left'
                        },
                    }
                });
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
        return <div style={{ textAlign: "center" }}>No data to display.</div>;
    }
}
export default Chart;