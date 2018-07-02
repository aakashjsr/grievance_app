function randomColor() {
    return "rgb(" + Math.floor(Math.random() * 256) + "," + Math.floor(Math.random() * 256) + "," + Math.floor(Math.random() * 256) + ",0.5)"
}

function computeData() {
    selectedProjects = $(".multi-select-1").select2("val");
    selectedCategories = $(".multi-select-2").select2("val");

    var dataSets = [];
    for(index=0; index < selectedProjects.length; index++) {
        var dataPoints = []
        for (sub_index=0; sub_index < selectedCategories.length; sub_index++) {

            dataPoints.push(appData[selectedProjects[index]][selectedCategories[sub_index]])
        }
        item = {label: selectedProjects[index],backgroundColor: randomColor(), data: dataPoints}
        dataSets.push(item);
    }

    var data = {
    labels: selectedCategories,
    datasets: dataSets
};
    return data;
}
var ctx = document.getElementById("myChart").getContext("2d");
var myBarChart;
function renderChart() {
    if (myBarChart) {
        myBarChart.destroy();
    }
    myBarChart = new Chart(ctx, {
    type: 'bar',
    data: computeData(),
});
}

$("document").ready(function() {
   $(".multi-select-1").select2();
   $(".multi-select-2").select2();
   $("#filter").on("click", renderChart);
   renderChart();
});