

def cart_items_count(request):
    cart = request.session.get('cart', {})
    
    total_item = sum(cart.values()) 
  
    return {'cart_items_count': total_item}