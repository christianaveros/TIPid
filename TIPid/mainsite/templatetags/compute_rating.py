from django import template

register = template.Library()

@register.filter
def compute_rating(value):
    return float(value) / 5.0 * 75.0

@register.assignment_tag
def items(best_deals, price_candidates, review_candidates, *args, **kwargs):
		price = 0
		reviews = 0
		for bd in best_deals:
				if bd in price_candidates:
						price = price + 1
				if bd in review_candidates:
						reviews = reviews + 1
		return 'price candidates in best deals: ' + str(price) + ' review candidates in best deals: ' + str(reviews)
