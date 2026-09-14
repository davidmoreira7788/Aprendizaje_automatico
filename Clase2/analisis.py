import pandas as pd
import json

# ------------------------------------------------------------------
# 1. Cargar datos de VENTAS desde el archivo CSV
# ------------------------------------------------------------------
df_ventas = pd.read_csv('ventas.csv', encoding='utf-8')

print("=" * 60)
print("1) VISTA PREVIA DE VENTAS (ventas.csv)")
print("=" * 60)
print(df_ventas.head())
print(f"\nForma del dataset: {df_ventas.shape[0]} filas x {df_ventas.shape[1]} columnas")

# ------------------------------------------------------------------
# 2. Cargar datos de CLIENTES desde el archivo JSON
# ------------------------------------------------------------------
df_clientes = pd.read_json('clientes.json', encoding='utf-8')

print("\n" + "=" * 60)
print("2) CLIENTES (clientes.json)")
print("=" * 60)
print(df_clientes.head())
print(f"\nCantidad total de clientes: {df_clientes.shape[0]}")

# ------------------------------------------------------------------
# 3. Cargar datos de INVENTARIO desde el archivo Excel
# ------------------------------------------------------------------
df_inventario = pd.read_excel('inventario.xlsx', sheet_name='Inventario')

print("\n" + "=" * 60)
print("3) INVENTARIO (inventario.xlsx)")
print("=" * 60)
print(df_inventario.head())
promedio_stock = df_inventario['stock_disponible'].mean()
print(f"\nPromedio de stock disponible para todos los productos: {promedio_stock:.2f} unidades")

# ------------------------------------------------------------------
# EXTRA: Combinar los 3 datasets en una única estructura
# ------------------------------------------------------------------
# Ventas + Clientes (por id_cliente)
df_ventas_clientes = df_ventas.merge(df_clientes, on='id_cliente', how='left')

# Agregamos info de inventario (por nombre de producto)
df_completo = df_ventas_clientes.merge(
    df_inventario[['producto', 'categoria']],
    on='producto', how='left'
)

print("\n" + "=" * 60)
print("DATASET COMBINADO (ventas + clientes + inventario)")
print("=" * 60)
print(df_completo.head())
print(f"\nForma del dataset combinado: {df_completo.shape[0]} filas x {df_completo.shape[1]} columnas")
