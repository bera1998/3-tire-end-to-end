function buyNow(flowerName) {
  fetch('/api/order', {
    method: 'POST',
    headers: {
      'Content-Type': 'application/json'
    },
    body: JSON.stringify({
      product: flowerName
    })
  })
  .then(res => res.json())
  .then(data => alert(data.message))
  .catch(err => alert('Order failed'));
}
