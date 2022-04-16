(function () {
  async function loadMap() {
    const topology = await fetch("/?data=county").then((response) =>
      response.json()
    );

    const data = [
      ["cu-ho", 10],
      ["be-3534", 11],
      ["be-3528", 12],
      ["be-3529", 13],
      ["be-3532", 14],
      ["be-489", 15],
      ["be-3535", 16],
      ["be-490", 17],
      ["be-3526", 18],
      ["be-3527", 19],
      ["be-3533", 20],
    ];

    Highcharts.mapChart("map-born", {
      chart: {
        map: topology,
      },

      title: {
        text: "Registros por provincia",
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
          data: data,
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
        text: "Registros por provincia",
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
          data: data,
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
