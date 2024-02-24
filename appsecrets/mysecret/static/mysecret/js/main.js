document.addEventListener('DOMContentLoaded', ()=>{
	const date_val = new Date();
	document.querySelector('span#year').textContent = date_val.getFullYear();
});