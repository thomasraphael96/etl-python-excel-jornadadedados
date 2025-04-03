from pydantic import BaseModel, Field, field_validator
from datetime import date
from typing import Optional
import math
import pandas as pd

# O ... (três pontos) no Pydantic indica que o campo é obrigatório e não pode ser None ou ausente nos dados de entrada.
class PlanilhaVendas(BaseModel):
    Organizador: int = Field(..., description="Identificador do organizador")
    Ano_Mes: str = Field(..., description="Ano e mês da campanha")
    Dia_da_Semana: str = Field(..., description="Dia da semana")
    Tipo_Dia: str = Field(..., description="Classificação do dia")
    Objetivo: str = Field(..., description="Objetivo da campanha")
    Date: date = Field(..., description="Data da campanha")
    AdSet_name: str = Field(..., description="Nome do conjunto de anúncios")
    Amount_spent: float = Field(0.0, ge=0, le=1200, description="Quantia gasta na campanha")
    Link_clicks: Optional[int] = Field(None, description="Número de cliques no link")
    Impressions: int = Field(..., description="Número de impressões")
    Conversions: Optional[int] = Field(None, description="Número de conversões")
    Segmentação: str = Field(..., description="Segmentação do público")
    Tipo_de_Anúncio: str = Field(..., description="Tipo de anúncio")
    Fase: str = Field(..., description="Fase da campanha")

    @field_validator("Link_clicks", "Conversions", mode="before")
    @classmethod
    def convert_nan_to_none(cls, value):
        """ Converte NaN para None antes da validação """
        return None if isinstance(value, float) and math.isnan(value) else value
    
    @classmethod
    def validar_colunas(cls, dataset: pd.DataFrame):
        """Verifica se todas as colunas esperadas estão no dataset"""
        colunas_esperadas = [
            "Organizador", "Ano_Mes", "Dia_da_Semana", "Tipo_Dia", "Objetivo", "Date",
            "AdSet_name", "Amount_spent", "Link_clicks", "Impressions", "Conversions",
            "Segmentação", "Tipo_de_Anúncio", "Fase"
        ]
        colunas_faltando = set(colunas_esperadas) - set(dataset.columns)
        if colunas_faltando:
            raise ValueError(f"Colunas ausentes no dataset: {', '.join(colunas_faltando)}")
        return True