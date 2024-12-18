from django import template

register = template.Library()

@register.filter
def format_currency(value):
    """Formatea un número como moneda en el formato $1.234,56."""
    try:
        value = float(value)
        # Separar la parte entera y decimal
        entero, decimal = f"{value:.2f}".split(".")
        # Formatear la parte entera con puntos
        entero_formateado = f"{int(entero):,}".replace(",", ".")
        return f"$ {entero_formateado},{decimal}"
    except (ValueError, TypeError):
        return value  # Devuelve el valor sin formato si no es un número
