swipeInterval = setInterval(autoScroll, 2000)
var current_page=0

function autoScroll(){

		if (current_page== 0) {
			document.querySelectorAll("main")[0].scroll(document.querySelectorAll("main")[0].offsetWidth,0)
			available=document.querySelectorAll(".slider")[0].offsetWidth-document.querySelectorAll(".slider img")[0].offsetWidth
			document.querySelectorAll(".slider img")[0].style.translate=" "+available+"px 0"
			current_page=1
		}else{
			document.querySelectorAll("main")[0].scroll(0,0)
			document.querySelectorAll(".slider img")[0].style.translate="0"
			current_page=0
		}
}