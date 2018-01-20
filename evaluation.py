from sklearn import metrics

def evaluate_ocr_prediction(expected, predicted):
    report = metrics.classification_report(expected, predicted)
    confusion_matrix = metrics.confusion_matrix(expected, predicted)
    return report, confusion_matrix

def main():
    expected = ["a", "b", "c", "d", "e"]
    predicted = ["a", "b", "c", "g", "e"]
    report, confusion_matrix = evaluate_ocr_prediction(expected, predicted)
    print report
    print confusion_matrix

if __name__ == "__main__":
    main()
