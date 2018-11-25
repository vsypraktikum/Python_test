//Globale Variablen
var Auswahl;

function markRow(id){
	if(Auswahl || Auswahl==0){
		let oldrow = document.getElementById(Auswahl);
		oldrow.className = "noMark";
	}
	if(Auswahl != id){
		Auswahl=id;
		var row = document.getElementById(id);
		row.className = "Mark";
	}else{
		Auswahl = undefined;
		var row = document.getElementById(id);
		row.className = "noMark";	
	}
}

function delRow(event_opl){
	if(Auswahl || Auswahl==0){
		if(confirm("Are you sure?")){
			alert("deleted")
			window.location = event_opl.target.id + Auswahl;
		}else{
			event_opl.preventDefault();
		}
	}else{
		alert("Keine Auswahl getroffen!")
	}
}

function editRow(event_opl){
	if(Auswahl || Auswahl==0){
		window.location = event_opl.target.id + Auswahl;
	}else{
		alert("Keine Auswahl getroffen!")
	}
}

function auswahl(event_opl){
	if(Auswahl || Auswahl==0){
		window.location = event_opl.target.id + Auswahl;
	}else{
		alert("Keine Auswahl getroffen!")
	}
}

function StandardListe_INIT(){
	let buttons = document.querySelectorAll("div.likeabutton");
	buttons[0].addEventListener('click', delRow, false);
	buttons[1].addEventListener('click', editRow, false);
	
}

function PPAngebot_INIT(){
	let buttons = document.querySelectorAll("div.likeabutton");
	buttons[0].addEventListener('click', auswahl, false);
	buttons[1].addEventListener('click', delRow, false);
	buttons[2].addEventListener('click', editRow, false);
	
}
