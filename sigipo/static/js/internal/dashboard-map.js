(function () {
  async function loadMap() {
    const topology = await fetch("?data=county").then((response) =>
      response.json()
    );
    const dataBorn = await fetch("?data=born").then((response) =>
      response.json()
    );
    const dataResidence = await fetch("?data=residence").then((response) =>
      response.json()
    );
    Highcharts.mapChart("map-born", {
      chart: {
        map: topology,
      },

      title: {
        text: "Registros por provincia natal",
      },

      subtitle: {
        text: "",
      },

      mapNavigation: {
        enabled: true,
        buttonOptions: {
          verticalAlign: "bottom",
        },
      },

      colorAxis: {
        min: 0,
        minColor: "#FF9090",
        maxColor: "#900000",
      },

      series: [
        {
          data: dataBorn,
          name: "Provincia natal",
          states: {
            hover: {
              color: "#D4AF37",
            },
          },
          dataLabels: {
            enabled: true,
            format: "{point.name}",
          },
        },
      ],
    });
    Highcharts.mapChart("map-residence", {
      chart: {
        map: topology,
      },

      title: {
        text: "Registros por provincia de residencia",
      },

      subtitle: {
        text: "",
      },

      mapNavigation: {
        enabled: true,
        buttonOptions: {
          verticalAlign: "bottom",
        },
      },

      colorAxis: {
        min: 0,
      },

      series: [
        {
          data: dataResidence,
          name: "Provincia de residencia",
          states: {
            hover: {
              color: "#D4AF37",
            },
          },
          dataLabels: {
            enabled: true,
            format: "{point.name}",
          },
        },
      ],
    });
  }
  loadMap();
})();
