"""EGX (Egyptian Exchange) sector classification for stock symbols."""
from __future__ import annotations
from typing import Dict, List, Set

# Sector mapping: sector name -> set of ticker symbols (without EGX: prefix)
EGX_SECTORS: Dict[str, Set[str]] = {
    "banks": {
        "COMI",  # Commercial International Bank
        "QNBE",  # QNB Alahli
        "ADIB",  # Abu Dhabi Islamic Bank Egypt
        "SAIB",  # Societe Arabe Internationale de Banque
        "HDBK",  # Housing & Development Bank
        "EGBE",  # Egyptian Gulf Bank
        "ARAB",  # Arab Investment Bank
        "ABUK",  # Abu Dhabi Islamic Bank - Misr
        "FAIT",  # Faisal Islamic Bank of Egypt
        "SAUD",  # Saudi Egyptian Finance
    },
    "real_estate": {
        "TMGH",  # Talaat Moustafa Group
        "ORHD",  # Orascom Development (Ora Developers)
        "PHDC",  # Palm Hills Development
        "EMFD",  # Emaar Misr
        "MNHD",  # Madinet Nasr Housing
        "OCDI",  # Orascom Construction & Development
        "HELI",  # Heliopolis Housing
        "ADRI",  # El Obour Real Estate
        "AREH",  # Arabia Real Estate
        "HDST",  # Hyde Park Development
        "PRCL",  # Porto Group
        "RREI",  # Rooya Real Estate
        "NAHO",  # Nasr City Housing
        "IDRE",  # Iwan Development
    },
    "financial_services": {
        "EFIH",  # EFG Hermes (Hermes Holding)
        "HRHO",  # EFG Hermes Holding
        "CIEB",  # CI Capital
        "CCAP",  # Corplease
        "INFI",  # Infinity
        "BTFH",  # Beltone Financial
        "EDFM",  # El Taameer Finance
        "ACAP",  # Arabia Capital
        "ICFC",  # Al Ahly for Finance & Investment
        "CNFN",  # Canal Finance
        "VALU",  # Valu (EFG Hermes fintech)
        "CFGH",  # CI Financial Group
    },
    "food_and_beverages": {
        "JUFO",  # Juhayna Food
        "EAST",  # Eastern Company (Tobacco)
        "SUGR",  # Delta Sugar
        "POUL",  # Cairo Poultry
        "CERA",  # Cairo for Oils
        "GOUR",  # Gourmet Egypt
        "MFPC",  # Middle East Food Products
        "AJWA",  # Ajwa Group
        "ISMA",  # Al-Ismaelia National Food
        "KABO",  # Kabo for Food
        "ELKA",  # El Kahera for Foods
    },
    "construction_and_materials": {
        "OCDI",  # Orascom Construction
        "SVCE",  # Suez Cement
        "SCEM",  # Sinai Cement
        "ARCC",  # Arabian Cement
        "IRON",  # Egyptian Iron & Steel
        "ALUM",  # Egypt Aluminum
        "CERA",  # Ceramica Cleopatra
        "MISR",  # Misr Cement
        "MBSC",  # Misr Beni Suef Cement
        "ETEL",  # El Ezz Steel
    },
    "telecommunications": {
        "ETEL",  # Telecom Egypt
        "ORWE",  # Orascom Investment Holding
        "RAYA",  # Raya Holding
        "MKIT",  # Mobikit
    },
    "energy_and_utilities": {
        "AMOC",  # Alexandria Mineral Oils
        "MOIL",  # Sidi Kerir Petrochemicals
        "TAQA",  # TAQA Arabia
        "EGAS",  # Egypt Gas
        "EGCH",  # Egyptian Chemical Industries
        "EPCO",  # Egyptian Petrochemicals
        "ELWA",  # El Wadi for Agro-Industrial
    },
    "healthcare_and_pharma": {
        "PHAR",  # Pharaon for Chemicals & Pharma
        "ISPH",  # Ibnsina Pharma
        "OCPH",  # October Pharma
        "SPMD",  # Speed Medical
        "AXPH",  # Alex Pharma
        "NIPH",  # Nile Pharma
        "BIOC",  # Bio-Diagnostics
        "MIPH",  # Medical International Pharma
    },
    "industrial": {
        "AMER",  # Amer Group
        "ELEC",  # El Sewedy Electric
        "GBCO",  # GB Auto (Ghabbour Auto)
        "MOED",  # Modern Egypt Development
        "ENGC",  # Engineering for the Petroleum
        "ACGC",  # Arab Cotton Ginning
        "AFDI",  # Al Ahram for Detergent Industries
        "KZPC",  # Kima (Aswan for Fertilizers)
        "GTEX",  # Golden Textiles
    },
    "technology": {
        "RAYA",  # Raya Holding (IT services)
        "FWRY",  # Fawry for Banking Technology
        "DGTZ",  # Digitize
        "SWDY",  # Swedy Electric (tech arm)
    },
    "tourism_and_entertainment": {
        "MHOT",  # Misr Hotels
        "ODIN",  # Odin Investments
        "LUTS",  # Lotus for Hotels
        "GTWL",  # Golden Pyramids Plaza
        "UTOP",  # Utopia
    },
    "textiles_and_clothing": {
        "GTEX",  # Golden Textiles
        "SPIN",  # Spinning & Weaving
        "NCCW",  # Nasr Clothing
        "ELNA",  # El Nasr Clothing & Textiles
    },
    "chemicals": {
        "EGCH",  # Egyptian Chemical Industries
        "KZPC",  # Kima (Fertilizers & Chemicals)
        "MFSC",  # Misr Fertilizers
        "AFMC",  # Alex Fertilizers & Chemicals
        "SCFM",  # South Cairo Flour Mills
    },
    "transportation_and_logistics": {
        "ALCN",  # Alexandria Containers
        "CSAG",  # Canal Shipping Agencies
        "EPPK",  # Egyptian Packing & Packaging
    },
}

# Reverse lookup: symbol -> sector
_SYMBOL_TO_SECTOR: Dict[str, str] = {}
for _sector, _symbols in EGX_SECTORS.items():
    for _sym in _symbols:
        if _sym not in _SYMBOL_TO_SECTOR:
            _SYMBOL_TO_SECTOR[_sym] = _sector


def get_sector(symbol: str) -> str:
    """Return the sector for an EGX symbol, or 'other' if not classified."""
    clean = symbol.upper().replace("EGX:", "")
    return _SYMBOL_TO_SECTOR.get(clean, "other")


def get_symbols_by_sector(sector: str) -> List[str]:
    """Return list of EGX symbols for a given sector."""
    symbols = EGX_SECTORS.get(sector.lower().replace(" ", "_"), set())
    return [f"EGX:{s}" for s in sorted(symbols)]


def get_all_sectors() -> List[str]:
    """Return list of all available EGX sectors."""
    return sorted(EGX_SECTORS.keys())
