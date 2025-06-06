document.addEventListener('DOMContentLoaded', function() {
  fetch('https://hellosalut.stefanbohacek.dev/?lang=fr')
    .then(response => {
      if (!response.ok) {
        throw new Error('Network response was not ok');
      }
      return response.json();
    })
    .then(data => {
      document.getElementById('hello').textContent = data.hello;
    })
    .catch(error => {
      console.error('There has been a problem with your fetch operation:', error);
    });
});
