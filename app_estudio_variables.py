#!/usr/bin/env python3
"""Aplicación interactiva para practicar variables en Python."""

from __future__ import annotations

from dataclasses import dataclass
from typing import Callable


@dataclass
class Ejercicio:
    titulo: str
    enunciado: str
    verificador: Callable[[str], bool]
    pista: str
    solucion: str


def normalizar(texto: str) -> str:
    return " ".join(texto.strip().lower().split())


def eq_estricto(esperado: str) -> Callable[[str], bool]:
    def verificador(respuesta: str) -> bool:
        return respuesta.strip() == esperado

    return verificador


def eq_flexible(*esperados: str) -> Callable[[str], bool]:
    normalizados = {normalizar(v) for v in esperados}

    def verificador(respuesta: str) -> bool:
        return normalizar(respuesta) in normalizados

    return verificador


def cargar_ejercicios() -> list[Ejercicio]:
    return [
        Ejercicio(
            titulo="1) Crear una variable",
            enunciado=(
                "Escribe una sola línea de código para guardar tu nombre en una variable "
                "llamada nombre con el valor Ana."
            ),
            verificador=eq_flexible("nombre = 'Ana'", 'nombre = "Ana"'),
            pista="Recuerda: variable = valor. El texto va entre comillas.",
            solucion="nombre = 'Ana'",
        ),
        Ejercicio(
            titulo="2) Variable numérica",
            enunciado=(
                "Crea una variable llamada edad y asígnale el número 16 (sin comillas)."
            ),
            verificador=eq_flexible("edad = 16"),
            pista="Los enteros no llevan comillas.",
            solucion="edad = 16",
        ),
        Ejercicio(
            titulo="3) Operar con variables",
            enunciado=(
                "Tienes: precio = 20 y descuento = 5. Escribe la línea para crear total "
                "con el resultado de restar descuento a precio."
            ),
            verificador=eq_flexible("total = precio - descuento"),
            pista="Crea una nueva variable usando una resta.",
            solucion="total = precio - descuento",
        ),
        Ejercicio(
            titulo="4) Actualizar una variable",
            enunciado=(
                "Si puntos empieza en 10, escribe la línea para sumar 1 usando el mismo "
                "nombre de variable."
            ),
            verificador=eq_flexible("puntos = puntos + 1", "puntos += 1"),
            pista="Puedes usar la forma larga o el operador abreviado +=.",
            solucion="puntos += 1",
        ),
        Ejercicio(
            titulo="5) Mostrar variables",
            enunciado=(
                "Escribe la línea para imprimir el valor de la variable mensaje."
            ),
            verificador=eq_flexible("print(mensaje)"),
            pista="Usa la función print(...).",
            solucion="print(mensaje)",
        ),
    ]


def intentar_ejercicio(ejercicio: Ejercicio) -> bool:
    print(f"\n{ejercicio.titulo}")
    print(ejercicio.enunciado)

    intentos = 0
    while True:
        respuesta = input("Tu respuesta (o escribe 'pista'): ").strip()
        if normalizar(respuesta) == "pista":
            print(f"💡 Pista: {ejercicio.pista}")
            continue

        intentos += 1
        if ejercicio.verificador(respuesta):
            print("✅ ¡Correcto!")
            return intentos == 1

        print("❌ No es correcto aún.")
        if intentos >= 2:
            ver_solucion = input("¿Quieres ver la solución? (s/n): ").strip().lower()
            if ver_solucion == "s":
                print(f"📘 Solución sugerida: {ejercicio.solucion}")


def main() -> None:
    print("=== Tutor de Variables en Python ===")
    print("Practicarás ejercicios cortos. Escribe 'pista' cuando necesites ayuda.")

    ejercicios = cargar_ejercicios()
    aciertos_primera = 0

    for ejercicio in ejercicios:
        if intentar_ejercicio(ejercicio):
            aciertos_primera += 1

    print("\n=== Resumen ===")
    print(f"Ejercicios completados: {len(ejercicios)}")
    print(f"Aciertos al primer intento: {aciertos_primera}")

    if aciertos_primera == len(ejercicios):
        print("🏆 ¡Excelente dominio de variables!")
    elif aciertos_primera >= 3:
        print("👏 ¡Muy bien! Sigue practicando para perfeccionar.")
    else:
        print("📚 Buen inicio. Repite los ejercicios y prueba nuevas variaciones.")


if __name__ == "__main__":
    main()
