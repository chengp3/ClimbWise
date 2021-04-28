function piefunc(...vars) {

    Chart.defaults.global.defaultFontFamily = "Georgia"
    Chart.defaults.global.legend.display = false;
/*
    let ctx10 = document.getElementById('chart3').getContext('2d');
    let data10 = {
        datasets: [{
            data: vars[2],
            backgroundColor: [
                'rgb(255, 99, 132)',
                'rgb(54, 162, 235)',
                'rgb(255, 205, 86)',
                'rgb(166,218,149)'
              ],
            borderColor: "rgb(50,50,50,.6)",
            borderWidth: 2
        }],
    
        // These labels appear in the legend and in the tooltips when hovering different arcs
        labels: vars[3]
    };

    let tenChart = new Chart(ctx10, {
        type: 'pie',
        data: data10,
        options: {
            responsive: false,
            title: {
                display: true,
                text: '5.10'
            }
        }
    });

    let ctx11 = document.getElementById('chart4').getContext('2d');
    let data11 = {
        datasets: [{
            data: vars[4],
            backgroundColor: [
                'rgb(255, 99, 132)',
                'rgb(54, 162, 235)',
                'rgb(255, 205, 86)',
                'rgb(166,218,149)'
              ],
            borderColor: "rgb(50,50,50,.6)",
            borderWidth: 2
        }],
    
        // These labels appear in the legend and in the tooltips when hovering different arcs
        labels: vars[5]
    };

    let eleChart = new Chart(ctx11, {
        type: 'pie',
        data: data11,
        options: {
            responsive: false,
            title: {
                display: true,
                text: '5.11'
            }
        }
    });

    let ctx12 = document.getElementById('chart5').getContext('2d');
    let data12 = {
        datasets: [{
            data: vars[6],
            backgroundColor: [
                'rgb(255, 99, 132)',
                'rgb(54, 162, 235)',
                'rgb(255, 205, 86)',
                'rgb(166,218,149)'
              ],
            borderColor: "rgb(50,50,50,.6)",
            borderWidth: 2
        }],
    
        // These labels appear in the legend and in the tooltips when hovering different arcs
        labels: vars[7]
    };

    let twelveChart = new Chart(ctx12, {
        type: 'pie',
        data: data12,
        options: {
            responsive: false,
            title: {
                display: true,
                text: '5.12'
            }
        }
    });
*/
    let ctxAll = document.getElementById('chart3').getContext('2d');
    let dataAll = {
        datasets: [{
            data: vars[0],
            backgroundColor: [
                '#003f5c',
                '#7a5195',
                '#ef5675',
                '#ffa600'
              ],
            borderColor: "rgb(255,255,255,1)",
            borderWidth: 1
        }],
    
        // These labels appear in the legend and in the tooltips when hovering different arcs
        labels: vars[1]
    };

    let allChart = new Chart(ctxAll, {
        type: 'pie',
        data: dataAll,
        options: {
            responsive: true,
            title: {
                display: false,
                text: 'All ticks'
            },
            tooltips: {
                custom: function(tooltip) {
                    if (!tooltip) return;
                    // disable displaying the color box;
                    tooltip.displayColors = false;
                }
            },
            plugins: {
                labels: [{
                    render: 'label',
                    arc: true,
                    fontColor: 'white',
                    position: 'outside'},{
                  render: 'percentage',
                  fontColor: 'white',
                  precision: 1
                }]
              },
        }
    });
}