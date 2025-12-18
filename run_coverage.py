import sys
import subprocess

try:
    import coverage
except Exception:
    print('`coverage` not found — installing via pip...')
    subprocess.check_call([sys.executable, '-m', 'pip', 'install', 'coverage'])
    import coverage

cov = coverage.Coverage()
cov.start()

import unittest
loader = unittest.TestLoader()
suite = loader.discover('.', pattern='test*.py')
runner = unittest.TextTestRunner(verbosity=2)
result = runner.run(suite)

cov.stop()
cov.save()

print('\nCoverage report (terminal):')
cov.report()

try:
    cov.html_report(directory='htmlcov')
    print("HTML report written to ./htmlcov/index.html")
except Exception:
    pass

if not result.wasSuccessful():
    sys.exit(1)
