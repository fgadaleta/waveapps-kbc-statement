from argparse import ArgumentParser
import pandas as pd
import logging


logging.basicConfig(level=logging.DEBUG)
log = logging.getLogger(__name__)


if __name__ == "__main__":
    parser = ArgumentParser()
    parser.add_argument('-i', '--input', dest='in_file', help='Input file to convert', required=True)
    parser.add_argument('-o', '--output', dest='out_file', help='Output file to store converted data', required=True)
    args = parser.parse_args()

    inpath = args.in_file
    outpath = args.out_file

    # Load pre-processed data
    log.info('Loading pre-processed data from %s', inpath)

    dat = pd.read_csv(inpath, sep=';')
    dat.rename(columns={'Account number': 'Account', 'credit': 'Deposits', 'debit': 'Withdrawals'}, inplace=True)
    dat = dat[['Account', 'Date', 'Description', 'Deposits', 'Withdrawals']]

    dat['Deposits'] = dat['Deposits'].replace(r'\s+', '0', regex=True)
    dat['Withdrawals'] = dat['Withdrawals'].replace(r'\s+', '0', regex=True)
    dat['Withdrawals'] = dat['Withdrawals'].replace(r'\s+', '0', regex=True)
    dat['Deposits'] = dat['Deposits'].replace(r'\s+', '0', regex=True)
    dat['Withdrawals'] = dat['Withdrawals'].apply(lambda x: x.replace(',','.'))
    dat['Deposits'] = dat['Deposits'].apply(lambda x: x.replace(',','.'))
    dat['Withdrawals'] = dat['Withdrawals'].apply(pd.to_numeric)
    dat['Deposits'] = dat['Deposits'].apply(pd.to_numeric)
    dat['Amount'] = dat['Deposits'] + dat['Withdrawals']
    dat = dat[['Account', 'Date', 'Description', 'Amount']]
    log.info('Saving to  %s', outpath)
    dat.to_csv(outpath, sep=',', index=False)
