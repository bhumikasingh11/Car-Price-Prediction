document.addEventListener('DOMContentLoaded', function () {
    const form = document.querySelector('form');

    form.addEventListener('submit', function (e) {
        const presentPrice = parseFloat(document.getElementById('present_price').value);
        const kmsDriven = parseFloat(document.getElementById('kms_driven').value);
        const yearsUsed = parseFloat(document.getElementById('years_used').value);

        if (presentPrice < 0 || kmsDriven < 0 || yearsUsed < 0) {
            e.preventDefault();
            alert('Please enter positive values only.');
        }
    });
});