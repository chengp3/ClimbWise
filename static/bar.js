function barfunc(...vars){

    Chart.defaults.global.defaultFontFamily = "Poppins";
    Chart.defaults.global.legend.display = false;

    let ctx = document.getElementById('chart2').getContext('2d');

    function getRandomColor() {
        let color = "rgba(";
        for (let i = 0; i < 3; i++) {
          color += (`${Math.floor(Math.random() * 255)}` + ',');
        }
        color += '.6)'
        return color;
      }

    let colors = []
    for (let i = 0; i < vars[0].length; i++){
        colors.push(getRandomColor())
    }
    
    let bordercolors = []

    colors.forEach(color => bordercolors.push(color.slice(0,-3) + '1)'))


const gradeConversion = {0: "Easy", 1: "5.1", 2: "5.2", 3: "5.3", 4: "5.4", 5: "5.5", 6: "5.6", 7: "5.7", 8: "5.8", 9: "5.9", 10: "5.10a", 11: "5.10b", 12: "5.10b/c", 13: "5.10c", 14: "5.10d", 15: "5.11a", 16: "5.11b", 17: "5.11b/c", 18: "5.11c", 19: "5.11d", 20: "5.12a", 21: "5.12b", 22: "5.12b/c", 23: "5.12c", 24: "5.12d", 25: "5.13a", 26: "5.13b", 27: "5.13b/c", 28: "5.13c", 29: "5.13d", 30: "5.14a", 31: "5.14b", 32: "5.14b/c", 33: "5.14c", 34: "5.14d", 35: "5.15a", 36: "5.15b", 37: "5.15b/c", 38: "5.15c", 39: "5.15d", 40: "5.16a", 41: "5.16b", 42: "5.16b/c"}

    let pyramid = new Chart(ctx, {
        type: 'horizontalBar',
        data: {
            labels: vars[0],
            datasets: [
              {
                data: vars[1],
                backgroundColor: 'white',
                borderColor: 'white',
                borderWidth: 0,
                hoverBorderWidth: 0,
                hoverBorderRadius: 5,
                hoverBackgroundColor: colors
              }
            ]
          },
        options: {
            responsive: true,
            title: {
                display: false,
                text: 'Climbs By Grade'
            },
            tooltips: {
                custom: function(tooltip) {
                    if (!tooltip) return;
                    // disable displaying the color box;
                    tooltip.displayColors = false;
                },
                callbacks: {
                    title: function(tooltipItem) {
                        return gradeConversion[tooltipItem[0].label];
                    },
                    label: function(tooltipItem) {
                        return `Number of sends: ${tooltipItem.value}`
                    }
                }
            },
            scales: {
                yAxes: [{
                    gridLines: {
                        lineWidth: 1,
                        zeroLineColor: 'rgba(255,255,255,.1)'
                    },
                    ticks: {
                        fontSize:12,
                    beginAtZero: true,
                    callback: function(value) {
                        return gradeConversion[value];
                        }
                    }
                }],
                xAxes: [{
                    gridLines: { 
                        lineWidth: 1,
                        color: 'rgba(255,255,255,.1)', 
                        zeroLineColor: 'rgba(255,255,255,.1)'
                    },
                }],
            }
        }
    });

}