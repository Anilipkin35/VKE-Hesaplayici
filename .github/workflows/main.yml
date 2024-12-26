name: VKE Hesaplama Workflow

on:
  workflow_dispatch:  # Manuel olarak tetiklenebilir

jobs:
  run-vke-script:
    runs-on: ubuntu-latest
    
    # Workflow parametreleri
    inputs:
      isim_soyisim:
        description: 'İsim ve Soyisim'
        required: true
        type: string
      boy:
        description: 'Boy (metre cinsinden, örneğin 1.75)'
        required: true
        type: number
      kilo:
        description: 'Kilo (kg cinsinden)'
        required: true
        type: number

    steps:
      - name: Checkout Repository
        uses: actions/checkout@v2
      
      - name: Run Python Script
        run: |
          python main.py "${{ github.event.inputs.isim_soyisim }}" ${{ github.event.inputs.boy }} ${{ github.event.inputs.kilo }}