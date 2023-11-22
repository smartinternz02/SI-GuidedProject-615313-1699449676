function previewImage(input) {
    const preview = document.getElementById('image-preview');
    preview.innerHTML = '';

    if (input.files && input.files[0]) {
        const reader = new FileReader();

        reader.onload = function (e) {
            const img = document.createElement('img');
            img.src = e.target.result;
            img.style.maxWidth = '100%';
            preview.appendChild(img);
        };

        reader.readAsDataURL(input.files[0]);
    }
}

function predict(event) {
    event.preventDefault();  // Prevent the default form submission behavior

    const form = document.getElementById('upload-form');
    const resultElement = document.getElementById('result');

    const formData = new FormData(form);
    fetch('/predict', {
        method: 'POST',
        body: formData
    })
    .then(response => response.json())
    .then(data => {
        resultElement.innerText = 'Prediction: ' + data.prediction;
    })
    .catch(error => console.error('Error:', error));
}
