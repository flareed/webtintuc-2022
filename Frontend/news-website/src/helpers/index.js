let exports = {};

exports.toSlug = (str) => {
	// Chuyển hết sang chữ thường
	str = str.toLowerCase();     
 
	// xóa dấu
	str = str
		.normalize('NFD') // chuyển chuỗi sang unicode tổ hợp
		.replace(/[\u0300-\u036f]/g, ''); // xóa các ký tự dấu sau khi tách tổ hợp
 
	// Thay ký tự đĐ
	str = str.replace(/[đĐ]/g, 'd');
	
	// Xóa ký tự đặc biệt
	str = str.replace(/([^0-9a-z-\s])/g, '');
 
	// Xóa khoảng trắng thay bằng ký tự -
	str = str.replace(/(\s+)/g, '-');
	
	// Xóa ký tự - liên tiếp
	str = str.replace(/-+/g, '-');
 
	// xóa phần dư - ở đầu & cuối
	str = str.replace(/^-+|-+$/g, '');
 
	// return
	return str;
}

exports.parseDate = (time) => {
	let date = new Date(time)
	let day = date.getDate();
	let month = date.getMonth() + 1;
	let year = date.getFullYear();

	const weekday = ["Chủ nhật", "Thứ hai", "Thứ ba", "Thứ tư", "Thứ năm", "Thứ sáu", "Thứ bảy"];
	let dayOfWeek = weekday[date.getDay()];

	let hr = ("0" + date.getHours()).slice(-2);
	let min = ("0" + date.getMinutes()).slice(-2);

	return `${dayOfWeek}, ${day}/${month}/${year}, ${hr}:${min}`
}

exports.parseDateSmaller = (time) => {
	let date = new Date(time)
	let day = date.getDate();
	let month = date.getMonth() + 1;
	let year = date.getFullYear();

	let hr = ("0" + date.getHours()).slice(-2);
	let min = ("0" + date.getMinutes()).slice(-2);

	return `${day}/${month}/${year}, ${hr}:${min}`
}

export default exports