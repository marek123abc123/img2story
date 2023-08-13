function processImage() {
    var input = document.getElementById('imageInput');
    var output = document.getElementById('output');
    var selectedImage = document.getElementById('selectedImage');

    var file = input.files[0];
    var reader = new FileReader();

    reader.onload = function (e) {
        var imageBase64 = e.target.result;

        selectedImage.src = imageBase64;
        selectedImage.style.display = 'block';

        eel.process_image(imageBase64)(function (result) {
            output.value = result;
        });
    };

    reader.readAsDataURL(file);
}

function generateStory() {
    var output = document.getElementById('output');

    eel.generate_story()(function (result) {
        output.value += result;
    });
}