(function () {
  async function loadCharts() {
    const topTen = await fetch("?data=top10").then((response) =>
      response.json()
    );

    const categories = topTen.map(
      (location) => location["primary_site__description"]
    );

    const lessThan20 = topTen.map((location) => location["less_than_20"]);
    const patientIn20 = topTen.map((location) => location["patient_in_20s"]);
    const patientIn30 = topTen.map((location) => location["patient_in_30s"]);
    const patientIn40 = topTen.map((location) => location["patient_in_40s"]);
    const patientIn50 = topTen.map((location) => location["patient_in_50s"]);
    const patientIn60 = topTen.map((location) => location["patient_in_60s"]);
    const patientIn70 = topTen.map((location) => location["patient_in_70s"]);
    const moreThan80 = topTen.map(
      (location) => location["patient_more_than_80s"]
    );

    Highcharts.chart("chart-top-10", {
      chart: {
        type: "column",
      },
      title: {
        text: "Las 10 localizaciones más afectadas por edades",
      },
      xAxis: {
        categories: categories,
        crosshair: true,
      },
      yAxis: {
        min: 0,
        title: {
          text: "Registros",
        },
      },
      tooltip: {
        headerFormat: '<span style="font-size:10px">{point.key}</span><table>',
        pointFormat:
          '<tr><td style="color:{series.color};padding:0">{series.name}: </td>' +
          '<td style="padding:0"><b>{point.y} mm</b></td></tr>',
        footerFormat: "</table>",
        shared: true,
        useHTML: true,
      },
      plotOptions: {
        column: {
          pointPadding: 0.2,
          borderWidth: 0,
        },
      },
      series: [
        { name: "<20", data: lessThan20 },
        { name: "20-29", data: patientIn20 },
        { name: "30-39", data: patientIn30 },
        { name: "40-49", data: patientIn40 },
        { name: "50-59", data: patientIn50 },
        { name: "60-69", data: patientIn60 },
        { name: "70-79", data: patientIn70 },
        { name: ">80", data: moreThan80 },
      ],
    });
    const ages = await fetch("?data=ages").then((response) => response.json());
    Highcharts.chart("chart-ages", {
      chart: {
        plotBackgroundColor: null,
        plotBorderWidth: null,
        plotShadow: false,
        type: "pie",
      },
      title: {
        text: "Porcentaje de diagnósticos por edades.",
      },
      tooltip: {
        pointFormat: "{series.name}: <b>{point.percentage:.1f}%</b>",
      },
      accessibility: {
        point: {
          valueSuffix: "%",
        },
      },
      plotOptions: {
        pie: {
          allowPointSelect: true,
          cursor: "pointer",
          dataLabels: {
            enabled: true,
            format: "<b>{point.name}</b>: {point.percentage:.1f} %",
          },
        },
      },
      series: [
        {
          name: "Porcentaje",
          colorByPoint: true,
          data: [
            {
              name: "<20",
              y: ages["less_than_20"] / ages["num_subjects"],
            },
            {
              name: "20-29",
              y: ages["patient_in_20s"] / ages["num_subjects"],
            },
            {
              name: "30-39",
              y: ages["patient_in_30s"] / ages["num_subjects"],
            },
            {
              name: "40-49",
              y: ages["patient_in_40s"] / ages["num_subjects"],
            },
            {
              name: "50-59",
              y: ages["patient_in_50s"] / ages["num_subjects"],
            },
            {
              name: "60-69",
              y: ages["patient_in_60s"] / ages["num_subjects"],
            },
            {
              name: "70-79",
              y: ages["patient_in_70s"] / ages["num_subjects"],
            },
            {
              name: ">80",
              y: ages["patient_more_than_80s"] / ages["num_subjects"],
            },
          ],
        },
      ],
    });
    window.chart_loaded = true;
    if (window.map_loaded && window.chart_loaded) {
      document.getElementById("id_loading").remove();
    }
  }
  loadCharts();
})();
