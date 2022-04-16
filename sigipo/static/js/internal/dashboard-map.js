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

    Highcharts.mapChart("container", {
      chart: {
        map: topology,
      },

      title: {
        text: "Highcharts Maps basic demo",
      },

      subtitle: {
        text: 'Source map: <a href="http://code.highcharts.com/mapdata/countries/be/be-all.topo.json">Belgium</a>',
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
          name: "Random data",
          states: {
            hover: {
              color: "#BADA55",
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
