// Global parameters:
// do not resize the chart canvas when its container does (keep at 400x400px)
// Chart.defaults.global.responsive = false;
 
// define the chart data
function linefunc(...vars) {

    Chart.defaults.global.defaultFontFamily = "Poppins"
    Chart.defaults.global.legend.display = false;

    let months = []

    vars[0].forEach(function(monthYear){
        let month = new Date(monthYear).toLocaleDateString('en-us',
        {
            year: 'numeric',
            month: 'long',
        })
        months.push(month)
    })

    let ctx = document.getElementById('chart1').getContext('2d');

    const gradeConversion = {0: "Easy", 1: "5.1", 2: "5.2", 3: "5.3", 4: "5.4", 5: "5.5", 6: "5.6", 7: "5.7", 8: "5.8", 9: "5.9", 10: "5.10a", 11: "5.10b", 12: "5.10b/c", 13: "5.10c", 14: "5.10d", 15: "5.11a", 16: "5.11b", 17: "5.11b/c", 18: "5.11c", 19: "5.11d", 20: "5.12a", 21: "5.12b", 22: "5.12b/c", 23: "5.12c", 24: "5.12d", 25: "5.13a", 26: "5.13b", 27: "5.13b/c", 28: "5.13c", 29: "5.13d", 30: "5.14a", 31: "5.14b", 32: "5.14b/c", 33: "5.14c", 34: "5.14d", 35: "5.15a", 36: "5.15b", 37: "5.15b/c", 38: "5.15c", 39: "5.15d", 40: "5.16a", 41: "5.16b", 42: "5.16b/c"}

    let myChart = new Chart(ctx, {
        type: 'line',
        data: {
            labels: months,
            datasets: [{
            label: 'Recent Best',
            pointBackGroundColor: "rgba(255,255,255,.5)",
            pointBorderColor: "rgba(255,255,255,1)",
            borderColor: "rgba(255,255,255,1)",
            data: vars[2],
            borderWidth: 1,
            lineTension: .3,
            fill: false,
            hoverBackgroundColor: "rgba(255,0,0,.5)",
            hoverBorderColor: "rgba(255,0,0,.5)"

            }]
        },
        options: {
            responsive: true,
            layout: {
                padding: {
                    bottom: 10
                }
            },
            tooltips: {
                custom: function(tooltip) {
                    if (!tooltip) return;
                    // disable displaying the color box;
                    tooltip.displayColors = false;
                },
                callbacks: {
                    label: function(context) {
                        return gradeConversion[context.value];
                    },
                }
            },
            scales: {
                xAxes: [{
                    gridLines: { lineWidth: 1,
                    color: 'rgba(255,255,255,.1)', 
                    zeroLineColor: 'rgba(255,255,255,.1)'
                    },
                    ticks: {
                        fontSize: 12,
                        callback: function(tick, index, array){
                            return (index % 4) ? "" : tick;
                        }
                    }
                }],
                yAxes: [{
                    gridLines: { lineWidth: 1,
                        color: 'rgba(255,255,255,.1)', 
                        zeroLineColor: 'rgba(255,255,255,.1)'
                        },
                    ticks: {
                        fontSize:14,
                        beginAtZero: true,
                        callback: function(value) {
                            return gradeConversion[value];
                        }
                    }
                }]
            }
        }
    })

    // what did vars contain?
    // vars[0] clearly a list of months, maybe datefill
    // vars[1] was highGradeList and vars[2] was recentGradeList
/*
        let months = []
        
        vars[0].forEach(function(monthYear){
            let month = new Date(monthYear).toLocaleDateString('en-us',
            {
                year: 'numeric',
                month: 'long',
            })
            months.push(month)
        })
        
        let ctx = document.getElementById('myChart').getContext('2d');

        let myChart = new Chart(ctx, {
            type: 'line',
            data: {
                labels: months,
                datasets: [{
                label: 'Personal best',
                pointBackGroundColor: "rgba(0,255,0,.5)",
                pointBorderColor: "rgba(0,255,0,1)",
                borderColor: "rgba(0,255,0,1)",
                data: vars[1],
                borderWidth: 1,
                lineTension: .3,
                fill: false
                },
                {label: 'Recent best',
                pointBackGroundColor: "rgba(255,0,0,.5)",
                pointBorderColor: "rgba(255,0,0,1)",
                borderColor: "rgba(255,0,0,1)",
                data: vars[2],
                borderWidth: 1,
                lineTension: .3,
                fill: false
                }]
            },
            options: {
                scales: {
                    xAxes: [{
                        ticks: {
                            callback: function(tick, index, array){
                                return (index % 4) ? "" : tick;
                            }
                        }
                    }],
                    yAxes: [{
                        ticks: {
                        beginAtZero: true,
                        callback: function(value) {
                            if (value === 5)
                                return '5.5';
                            else if (value === 10)
                                return '5.10a';
                            else if (value === 15)
                                return '5.11a';
                            else if (value === 20)
                                return '5.12a';
                            else if (value === 25)
                                return '5.13a';
                            else if (value === 30)
                                return '5.14a';
                            else if (value === 35)
                                return '5.15a';
                            else
                                return '';
                            }
                        }
                    }]
                }
            }
        })
        */
}
 
// get chart canvas
// let ctx = document.getElementById("myChart").getContext("2d");
 
// create the chart using the chart canvas

