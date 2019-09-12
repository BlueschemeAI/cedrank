$(document).ready(function() {
    "use strict";
    
    Deb_LineChart();
    Deb_PieChart()

});



function Deb_LineChart() {
  if ($( "#chart_line" ).length) {
    var ctx = document.getElementById('chart_line').getContext("2d");

    var gradientStroke = ctx.createLinearGradient(500, 0, 100, 0);
    var gradientStroke2 = ctx.createLinearGradient(500, 0, 100, 0);
    gradientStroke.addColorStop(0, '#51eca5');
    gradientStroke.addColorStop(1, '#2f1ce0');

    gradientStroke2.addColorStop(0, '#fad65f');
    gradientStroke2.addColorStop(1, '#f7701f');


    var myChart = new Chart(ctx, {
        type: 'line',
        data: {
            labels: ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '13', '14', '15', '16', '17', '18', '19', '20'],
            datasets: [{
                label: "Creditors",
                borderColor: gradientStroke2,
                pointBorderColor: gradientStroke2,
                pointBackgroundColor: gradientStroke2,
                pointHoverBackgroundColor: gradientStroke2,
                pointHoverBorderColor: gradientStroke2,
                pointBorderWidth: 10,
                pointHoverRadius: 10,
                pointHoverBorderWidth: 1,
                pointRadius: 3,
                fill: false,
                borderWidth: 4,
                data: [40, 43, 42, 40, 45, 60, 55, 50, 17, 20, 19, 15, 22, 27, 31, 16, 50, 61, 45, 52]
            },
            {
                label: "Debtors",
                borderColor: gradientStroke,
                pointBorderColor: gradientStroke,
                pointBackgroundColor: gradientStroke,
                pointHoverBackgroundColor: gradientStroke,
                pointHoverBorderColor: gradientStroke,
                pointBorderWidth: 10,
                pointHoverRadius: 10,
                pointHoverBorderWidth: 1,
                pointRadius: 3,
                fill: false,
                borderWidth: 4,
                data: [50, 35, 55, 56, 40, 42, 56, 40, 22, 52, 41, 46, 50, 40, 33, 34, 42, 46, 52, 42]
            }]
        },
        options: {          
            legend: {
                position: "top"
            },
            scales: {
                yAxes: [{
                    ticks: {
                        fontColor: "rgba(0,0,0,0.5)",
                        fontStyle: "bold",
                        beginAtZero: true,
                        padding: 20
                    }
                }],
                xAxes: [{
                    gridLines: {
                        zeroLineColor: "transparent"
                    },
                    ticks: {
                        padding: 20,
                        fontColor: "rgba(0,0,0,0.5)",
                        fontStyle: "bold"
                    }
                }]
            }
        }
    });
  }
}

function Deb_PieChart() {
  if ($( "#pieChart" ).length) {
    var ctx = document.getElementById('pieChart').getContext('2d');
    var chart = new Chart(ctx, {
        type: 'doughnut',

        data: {
          datasets: [{
            data: [95, 19],
            backgroundColor: [
                'rgb(73, 123, 245)',
                'rgb(119, 81, 227)'
            ]
        }],
          labels: [
              'Expense',
              'Income'
          ]
        },

        options: {
          legend: {
              position: "bottom"
          }
        }
    });
  }
}


/*jQuery(window).scroll(function() {
  if ($(window).scrollTop() > 70) {
      $('.fixed-top').addClass('bg-white navbar-light').removeClass('navbar-dark');
      $('.navbar-brand img').attr('src', 'assets/images/logo.png');
  } else {
      $('.fixed-top').removeClass('bg-white navbar-light').addClass('navbar-dark');
      $('.navbar-brand img').attr('src', 'assets/images/logo-white.png');
  }
});
$(document).ready(function() {
  $(".scroll-on").on('click', function(event) {

    if (this.hash !== "") {
      event.preventDefault();

      
      var hash = this.hash;
      $('html, body').animate({
        scrollTop: $(hash).offset().top
      }, 800, function(){
        window.location.hash = hash;
      });
    } 
  });
});
$('#navbarCollapse').on('show.bs.collapse', function () {
  $(this).closest('body').addClass('navbar-open');
})
$('#navbarCollapse').on('hide.bs.collapse', function () {
  $(this).closest('body').removeClass('navbar-open');
})*/
