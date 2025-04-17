#docker image build -t pythonconsole .
docker run  -v ./code:/code -v ./tweets:/tweets -v ./done:/done pythonconsole bash -c "python /code/workflows.py tweet"

