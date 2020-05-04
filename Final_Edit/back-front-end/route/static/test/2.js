// 检查浏览器是否支持拖放上传。
if('draggable' in document.createElement('span')){
　　var holder = document.getElementById('holder');
　　holder.ondragover = function () { this.className = 'hover'; return false; };
　　holder.ondragend = function () { this.className = ''; return false; };
　　holder.ondrop = function (event) {
　　　　event.preventDefault();
　　　　this.className = '';
　　　　var files = event.dataTransfer.files;
　　　　// do something with files
　　};
}