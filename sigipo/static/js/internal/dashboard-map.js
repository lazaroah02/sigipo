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
        minColor: "#9090FF",
        maxColor: "#000090",
      },

      series: [
        {
          data: dataBorn,
          name: "Provincia natal",
          states: {
            hover: {
              color: "#D437AF",
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
        minColor: "#FFE196",
        maxColor: "#FFA420",
      },

      series: [
        {
          data: dataResidence,
          name: "Provincia de residencia",
          states: {
            hover: {
              color: "#AFD437",
            },
          },
          dataLabels: {
            enabled: true,
            format: "{point.name}",
          },
        },
      ],
    });
    window.map_loaded = true;
    if (window.map_loaded && window.chart_loaded) {
      document.getElementById("id_loading").remove();
    }
  }
  loadMap();
})();
