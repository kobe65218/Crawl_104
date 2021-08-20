var canvas = document.getElementById("current_chart");
var ctx = canvas.getContext("2d");


window["chart"] = new Chart(ctx, {
    data: {
        labels: [0,10,20,30,40,50],
        datasets: [{
            type: 'line',
            label: "收盤價",
            lineTension: 0.3,
            backgroundColor: "rgba(78, 115, 223, 0.05)",
            borderColor: "rgba(78, 115, 223, 1)",
            pointRadius: 2,
            pointBackgroundColor: "rgba(78, 115, 223, 0.05)",
            pointBorderColor: "rgba(78, 115, 223, 1)",
            pointHoverRadius: 3,
            pointHoverBackgroundColor: "rgba(78, 115, 223, 1)",
            pointHoverBorderColor: "rgba(78, 115, 223, 1)",
            pointHitRadius: 10,
            pointBorderWidth: 2,
            data: [],
        }
        ],
    },
    options: {
        maintainAspectRatio: false,
        layout: {
            padding: {
                left: 5,
                right: 5,
                top: 0,
                bottom: 0
            }
        },
        scales: {
            xAxes: [{
                time: {
                    unit: 'date'
                }
                ,
                gridLines: {
                    display: true,
                    drawBorder: false
                },
                ticks: {
                    maxTicksLimit: 7,
                    display: true
                }
            }],
            yAxes: [{
                ticks: {
                    maxTicksLimit: 5,
                    padding: 0,
                    // Include a dollar sign in the ticks
                    // callback: function (value, index, values) {
                    //     return '$' + number_format(value);
                    // }
                },
                gridLines: {
                    color: "rgb(234, 236, 244)",
                    zeroLineColor: "rgb(234, 236, 244)",
                    drawBorder: false,
                    borderDash: [2],
                    zeroLineBorderDash: [2]
                }
            }],
        },
        legend: {
            display: false,
            align: "end",
            labels: {
                boxWidth: 80,
                usePointStyle: true,
                pointStyle: "circle",
            }


        },
        tooltips: {
            backgroundColor: "rgb(255,255,255)",
            bodyFontColor: "#858796",
            titleMarginBottom: 10,
            titleFontColor: '#6e707e',
            titleFontSize: 14,
            borderColor: '#dddfeb',
            borderWidth: 1,
            xPadding: 1,
            yPadding: 1,
            displayColors: false,
            intersect: false,
            mode: 'index',
            caretPadding: 10,
            // callbacks: {
            //     label: function (tooltipItem, chart) {
            //         var datasetLabel = chart.datasets[tooltipItem.datasetIndex].label || '';
            //         point = chart.datasets[tooltipItem.datasetIndex].pointRadius[tooltipItem.index]
            //         if (point == 3) {
            //
            //             return datasetLabel + ': $' + number_format(tooltipItem.yLabel) + " annnomy: True";
            //
            //         } else {
            //
            //             return datasetLabel + ': $' + number_format(tooltipItem.yLabel) + " annnomy:False ";
            //         }
            //         // var annomy = chart.dataIndex.pointRadius || '';
            //
            //     }
            // }
        }
    }
});

