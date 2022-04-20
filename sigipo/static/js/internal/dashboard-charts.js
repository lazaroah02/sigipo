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
  }
  loadCharts();
})();
