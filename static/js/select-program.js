// choose program and changing block bottom row
function openProgram(evt, blockName) {
    var i, tabcontent, tablinks;
    tabcontent = document.getElementsByClassName("your-programs-block");
    for (i = 0; i < tabcontent.length; i++) {
      tabcontent[i].style.display = "none";
    }
    tablinks = document.getElementsByClassName("tablinks-row-number");
    for (i = 0; i < tablinks.length; i++) {
      tablinks[i].className = tablinks[i].className.replace(" active", "");
    }
    document.getElementById(blockName).style.display = "block";
    evt.currentTarget.className += " active";
  }

//   default open 1st item
document.getElementById("defaultOpen").click();