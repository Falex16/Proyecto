import streamlit as st
import numpy as np
import pandas as pd

from libreria_funciones_proyecto1 import (
    calcular_ticket_promedio,
    calcular_margen_neto,
    calcular_tasa_crecimiento_ventas
)

from libreria_clases_proyecto1 import Empleado

# Configuración de la página
st.set_page_config(page_title="Proyecto Python Fundamentals", layout="wide")

# Menú lateral
menu = st.sidebar.selectbox(
    "Selecciona una opción",
    ["🏠 Home", "💰 Ejercicio 1", "📦 Ejercicio 2", "🧮 Ejercicio 3", "🗂️ Ejercicio 4"]
)

# HOME
if menu == "🏠 Home":

    col1, col2 = st.columns([1, 15])

    with col1:
        st.image("logo.png", width=80)

    with col2:
        st.title("Sistema de Análisis y Gestión Empresarial")

    st.subheader("👨‍💻 Datos Personales")
    st.write("Nombre: Fabrizio Peña Panduro")
    st.write("Módulo: Python Fundamentals")
    st.write("Año: 2026")
    
    st.subheader("📌 Descripción del Proyecto")
    st.write("""
    Esta aplicación fue desarrollada en Streamlit integrando conceptos de:
    - Variables
    - Estructuras de datos
    - Control de flujo
    - Funciones
    - Programación orientada a objetos (POO)
    """)
    
    st.subheader("🛠️ Tecnologías utilizadas")
    st.write("Python, Streamlit, NumPy, Pandas")






# EJERCICIO 1
elif menu == "💰 Ejercicio 1":
    st.title("💰 Flujo de Caja")

    # Descripción
    st.markdown("Registra ingresos y gastos para calcular el flujo de caja")

    # Inicializar lista
    if "movimientos" not in st.session_state:
        st.session_state.movimientos = []

    # Inputs
    concepto = st.text_input("Concepto")
    tipo = st.selectbox("Tipo de movimiento", ["Ingreso", "Gasto"])
    valor = st.number_input("Valor", min_value=0.0)

    # Botón agregar
    if st.button("Agregar movimiento"):
        if concepto != "" and valor > 0:
            st.session_state.movimientos.append({
                "Concepto": concepto,
                "Tipo": tipo,
                "Valor": valor
            })
            st.success("Movimiento agregado correctamente")
        else:
            st.error("Ingrese datos válidos")

    # Mostrar tabla
    if st.session_state.movimientos:
        st.subheader("📋 Movimientos registrados")
        st.dataframe(st.session_state.movimientos)

        # Cálculos
        total_ingresos = sum(m["Valor"] for m in st.session_state.movimientos if m["Tipo"] == "Ingreso")
        total_gastos = sum(m["Valor"] for m in st.session_state.movimientos if m["Tipo"] == "Gasto")
        saldo = total_ingresos - total_gastos

        # Métricas
        col1, col2, col3 = st.columns(3)

        with col1:
            st.metric("Ingresos", total_ingresos)

        with col2:
            st.metric("Gastos", total_gastos)

        with col3:
            st.metric("Saldo", saldo)

        # Estado final
        if saldo > 0:
            st.success("Flujo de caja a favor")
        elif saldo < 0:
            st.error("Flujo de caja en contra")
        else:
            st.info("Flujo de caja equilibrado")





# EJERCICIO 2
elif menu == "📦 Ejercicio 2":
    st.title("📦 Registro de Productos")

    # Descripción
    st.markdown("Registro de productos y visualización de las ventas")

    # Inicializar datos
    if "productos" not in st.session_state:
        st.session_state.productos = {
            "nombre": [],
            "categoria": [],
            "precio": [],
            "cantidad": [],
            "total": []
        }

    # Inputs
    nombre = st.text_input("Nombre del producto")
    categoria = st.selectbox("Categoría", ["Accesorios", "Ropa", "Alimentos", "Otros"])
    precio = st.number_input("Precio", min_value=0.0)
    cantidad = st.number_input("Cantidad", min_value=0)

    # Botón agregar
    if st.button("Agregar producto"):
        if nombre != "" and precio > 0 and cantidad > 0:
            total = precio * cantidad

            st.session_state.productos["nombre"].append(nombre)
            st.session_state.productos["categoria"].append(categoria)
            st.session_state.productos["precio"].append(precio)
            st.session_state.productos["cantidad"].append(cantidad)
            st.session_state.productos["total"].append(total)

            st.success("Producto agregado correctamente")
        else:
            st.error("Ingrese datos válidos")

    # Muestra DataFrame
    if len(st.session_state.productos["nombre"]) > 0:

        # Convertir a arrays NumPy
        nombres = np.array(st.session_state.productos["nombre"])
        categorias = np.array(st.session_state.productos["categoria"])
        precios = np.array(st.session_state.productos["precio"])
        cantidades = np.array(st.session_state.productos["cantidad"])
        totales = np.array(st.session_state.productos["total"])

        # DataFrame
        df = pd.DataFrame({
            "Producto": nombres,
            "Categoría": categorias,
            "Precio": precios,
            "Cantidad": cantidades,
            "Total": totales
        })

        st.subheader("📊 Lista de productos")
        st.dataframe(df)
        st.metric("💰 Total de ventas", sum(st.session_state.productos["total"]))








# EJERCICIO 3
elif menu == "🧮 Ejercicio 3":
    st.title("🧮 Análisis de Indicadores Comerciales")

    st.markdown("""
    Permite analizar indicadores comerciales clave y comprender mejor el comportamiento de las ventas y la rentabilidad
    """)

    import pandas as pd

    opcion = st.selectbox(
        "Selecciona la función",
        ["Ticket Promedio", "Margen Neto", "Crecimiento de Ventas"]
    )

  
    # 1. TICKET PROMEDIO

    if opcion == "Ticket Promedio":

        if "hist_ticket" not in st.session_state:
            st.session_state.hist_ticket = []

        ventas = st.number_input("Ventas totales", min_value=0.0)
        clientes = st.number_input("Número de clientes", min_value=1)

        if st.button("Calcular Ticket", key="btn_ticket"):
            try:
                res = calcular_ticket_promedio(ventas, clientes)

                st.success("Cálculo realizado correctamente")
                st.write("Ticket Promedio:", res["ticket_promedio"])

                st.session_state.hist_ticket.append({
                    "Ventas": ventas,
                    "Clientes": clientes,
                    "Ticket Promedio": res["ticket_promedio"]
                })

            except Exception as e:
                st.error(str(e))

        if len(st.session_state.hist_ticket) > 0:
            df = pd.DataFrame(st.session_state.hist_ticket)

            st.subheader("📊 Histórico de resultados")
            st.dataframe(df)

  
    # 2. MARGEN NETO

    elif opcion == "Margen Neto":

        if "hist_margen" not in st.session_state:
            st.session_state.hist_margen = []

        ingresos = st.number_input("Ingresos", min_value=0.0)
        costos = st.number_input("Costos", min_value=0.0)
        gastos = st.number_input("Gastos operativos", min_value=0.0)
        impuestos = st.number_input("Impuestos", min_value=0.0)

        if st.button("Calcular Margen", key="btn_margen"):
            try:
                res = calcular_margen_neto(ingresos, costos, gastos, impuestos)

                st.success("Cálculo realizado correctamente")
                st.write("Utilidad Bruta:", res["utilidad_bruta"])
                st.write("Utilidad Neta:", res["utilidad_neta"])
                st.write("Margen Neto (%):", res["margen_neto_pct"])

                st.session_state.hist_margen.append({
                    "Ingresos": ingresos,
                    "Margen Neto (%)": res["margen_neto_pct"]
                })

            except Exception as e:
                st.error(str(e))

        if len(st.session_state.hist_margen) > 0:
            df = pd.DataFrame(st.session_state.hist_margen)

            st.subheader("📊 Histórico de resultados")
            st.dataframe(df)

 
    # 3. CRECIMIENTO DE VENTAS
 
    elif opcion == "Crecimiento de Ventas":

        if "hist_crecimiento" not in st.session_state:
            st.session_state.hist_crecimiento = []

        anterior = st.number_input("Ventas periodo anterior", min_value=0.0)
        actual = st.number_input("Ventas periodo actual", min_value=0.0)

        if st.button("Calcular Crecimiento", key="btn_crecimiento"):
            try:
                res = calcular_tasa_crecimiento_ventas(anterior, actual)

                st.success("Cálculo realizado correctamente")
                st.write("Crecimiento (%):", res["tasa_crecimiento_pct"])

                st.session_state.hist_crecimiento.append({
                    "Ventas Anteriores": anterior,
                    "Ventas Actuales": actual,
                    "Crecimiento (%)": res["tasa_crecimiento_pct"]
                })

            except Exception as e:
                st.error(str(e))

        if len(st.session_state.hist_crecimiento) > 0:
            df = pd.DataFrame(st.session_state.hist_crecimiento)

            st.subheader("📊 Histórico de resultados")
            st.dataframe(df)






# EJERCICIO 4
elif menu == "🗂️ Ejercicio 4":
    st.title("🗂️ CRUD Empleado")

    st.markdown("""
    CRUD: Permite crear, visualizar, actualizar y eliminar empleados.
    Al registrar por primera vez, en el apartado "Gestionar" se podrá actualizar y eliminar
    """)

    # Inicializar lista
    if "empleados" not in st.session_state:
        st.session_state.empleados = []

    # Tabs
    tab1, tab2, tab3 = st.tabs(["➕ Crear", "📋 Ver", "✏️ Gestionar"])


    # CREAR
   
    with tab1:
        st.subheader("➕ Registrar nuevo empleado")

        nombre = st.text_input("Nombre")
        salario = st.number_input("Salario base", min_value=0.0)
        bono = st.number_input("Bono (%)", min_value=0.0, max_value=100.0)
        descuento = st.number_input("Descuento (%)", min_value=0.0, max_value=100.0)

        if st.button("Guardar empleado"):
            try:
                nuevo = Empleado(nombre, salario, bono, descuento)
                st.session_state.empleados.append(nuevo)
                st.success("Empleado registrado correctamente")
                st.rerun()  # refresca inmediatamente
            except Exception as e:
                st.error(str(e))

 
    # VER
 
    with tab2:
        st.subheader("📋 Lista de empleados")

        if len(st.session_state.empleados) > 0:
            data = [emp.resumen() for emp in st.session_state.empleados]
            df = pd.DataFrame(data)
            st.dataframe(df)
        else:
            st.info("No hay empleados registrados")


    # GESTIONAR (UPDATE + DELETE)

    with tab3:
        st.subheader("✏️ Gestionar empleados")

        if len(st.session_state.empleados) > 0:

            # Tabla
            data = [emp.resumen() for emp in st.session_state.empleados]
            df = pd.DataFrame(data)
            st.dataframe(df)

            # Selección
            nombres = [emp.nombre for emp in st.session_state.empleados]
            seleccionado = st.selectbox("Selecciona un empleado", nombres)

            # Objeto
            empleado_sel = next(emp for emp in st.session_state.empleados if emp.nombre == seleccionado)

            st.markdown("### 🧾 Editar datos")

            nuevo_salario = st.number_input(
                "Salario base",
                value=empleado_sel.salario_base
            )

            nuevo_bono = st.number_input(
                "Bono (%)",
                value=empleado_sel.porcentaje_bono
            )

            nuevo_descuento = st.number_input(
                "Descuento (%)",
                value=empleado_sel.porcentaje_descuento
            )

            col1, col2 = st.columns(2)

            # ACTUALIZAR
            with col1:
                if st.button("✏️ Actualizar"):
                    empleado_sel.salario_base = nuevo_salario
                    empleado_sel.porcentaje_bono = nuevo_bono
                    empleado_sel.porcentaje_descuento = nuevo_descuento

                    st.success("Empleado actualizado correctamente")
                    st.rerun() 

            # ELIMINAR
            with col2:
                if st.button("🗑️ Eliminar"):
                    st.session_state.empleados = [
                        emp for emp in st.session_state.empleados if emp.nombre != seleccionado
                    ]

                    st.warning("Empleado eliminado correctamente")
                    st.rerun() 

        else:
            st.info("No hay empleados registrados")