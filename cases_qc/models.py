import uuid as uuid_object

from django.contrib.postgres.fields import ArrayField
from django.db import models
from django_pydantic_field import SchemaField
import pydantic

from cases.models import Case

#: Maximal array length for Postgres array fields
MAX_ARRAY_LENGTH = 10_000
#: Maximal length of metrics to read
MAX_METRIC_COUNT = 1000


class DragenStyleMetric(pydantic.BaseModel):
    """Pydantic model for Dragen-style quality control metric entries"""

    #: The section of the value
    section: str | None
    #: The "entry" in the section can be empty or the read group / sample
    entry: str | None
    #: The name of the metric
    name: str | None
    #: The count / ratio / time / etc. value
    value: int | float | str | None
    #: The count as percentage / seconds
    value_float: float | None = None


class DragenStyleCoverage(pydantic.BaseModel):
    """Pydantic model for Dragen-style coverage metric entries"""

    #: The contig name
    contig_name: str
    #: The contig length
    contig_len: int
    #: The mean coverage
    cov: float


class CaseQc(models.Model):
    """Quality control metrics set for one case."""

    #: Draft - is currently being built.
    STATE_DRAFT = "DRAFT"
    #: Active - is currently not active.
    STATE_ACTIVE = "ACTIVE"

    STATE_CHOICES = (
        (STATE_DRAFT, STATE_DRAFT),
        (STATE_ACTIVE, STATE_ACTIVE),
    )

    #: Record UUID.
    sodar_uuid = models.UUIDField(default=uuid_object.uuid4, unique=True)
    #: DateTime of creation.
    date_created = models.DateTimeField(auto_now_add=True)
    #: DateTime of last modification.
    date_modified = models.DateTimeField(auto_now=True)

    #: State of the QC set
    state = models.CharField(max_length=50, choices=STATE_CHOICES, default=STATE_DRAFT)
    #: The case this QC set belong to
    case = models.ForeignKey(Case, on_delete=models.CASCADE, null=False, blank=False)

    class Meta:
        #: Order by creation date
        ordering = ["-date_created"]


class CaseQcBaseModel(models.Model):
    """Base class for statistics associated with ``CaseQc``."""

    #: Record UUID.
    sodar_uuid = models.UUIDField(default=uuid_object.uuid4, unique=True)
    #: DateTime of creation.
    date_created = models.DateTimeField(auto_now_add=True)
    #: DateTime of last modification.
    date_modified = models.DateTimeField(auto_now=True)

    #: The QC metric set this histogram belongs to
    caseqc = models.ForeignKey(CaseQc, on_delete=models.CASCADE, null=False, blank=False)

    class Meta:
        abstract = True


class CaseQcForSampleBaseModel(CaseQcBaseModel):
    """Base class for statistics associated with ``CaseQc`` for one sample."""

    #: The sample this histogram belongs to
    sample = models.CharField(max_length=200, null=False, blank=False)

    class Meta:
        abstract = True


class DragenBaseHistogram(CaseQcForSampleBaseModel):
    """Base model for Dragen-style histograms


    The histogram is stored in a sparse fashion, storing values and their counts.  In the case of
    more than ``MAX_ARRAY_LENGTH`` entries, the histogram must be truncated which is done in the
    import code and which will truncate reading the lines.
    """

    #: The histogram keys
    keys = ArrayField(models.IntegerField(), null=False, blank=False, max_length=MAX_ARRAY_LENGTH)
    # The histogram values
    values = ArrayField(models.IntegerField(), null=False, blank=False, max_length=MAX_ARRAY_LENGTH)

    class Meta:
        abstract = True


class DragenBaseMetrics(CaseQcBaseModel):
    """Abstract metrics model not specific to one sample"""

    #: Metrics as JSON following the ``DragenStyleMetric`` schema
    metrics = SchemaField(schema=list[DragenStyleMetric], blank=False, null=False)

    class Meta:
        abstract = True


class DragenBaseMetricsForSample(CaseQcForSampleBaseModel):
    """Abstract metrics model for one sample in a case"""

    #: Metrics as JSON following the ``DragenStyleMetric`` schema
    metrics = SchemaField(schema=list[DragenStyleMetric], blank=False, null=False)

    class Meta:
        abstract = True


class DragenCnvMetrics(DragenBaseMetrics):
    """CNV metrics for one sample in a case"""


class DragenFragmentLengthHistogram(DragenBaseHistogram):
    """Histogram of fragment lengths for one sample in a case."""


class DragenMappingMetrics(DragenBaseMetricsForSample):
    """Metrics for the read mapping for one sample in the case"""


class DragenPloidyEstimationMetrics(DragenBaseMetricsForSample):
    """Ploidy estimation metrics for one sample in the case"""


class DragenRohMetrics(DragenBaseMetricsForSample):
    """ROH metrics for one sample in the case"""


class DragenVcHethomRatioMetrics(DragenBaseMetrics):
    """Per-contig het./hom. metrics for one sample in the case"""


class DragenVcMetrics(DragenBaseMetrics):
    """Variant calling metrics for one sample in the case"""


class DragenSvMetrics(DragenBaseMetrics):
    """SV calling metrics for one sample in the case"""


class DragenTimeMetrics(DragenBaseMetricsForSample):
    """Time metrics for one sample in the case"""


class DragenTrimmerMetrics(DragenBaseMetricsForSample):
    """Trimmer metrics for one sample in the case"""


class DragenWgsCoverageMetrics(DragenBaseMetricsForSample):
    """WGS coverage summary metrics for one sample in the case"""


class DragenWgsContigMeanCovMetrics(CaseQcForSampleBaseModel):
    """Contig-wise WGS coverage metrics for one sample in the case"""

    #: Metrics as JSON following the ``DragenStyleCoverage`` schema
    metrics = SchemaField(schema=list[DragenStyleCoverage], blank=False, null=False)


class DragenWgsOverallMeanCov(DragenBaseMetricsForSample):
    """Overall mean WGS coverage metrics for one sample in the case"""


class DragenWgsFineHist(DragenBaseHistogram):
    """Fine histogram of WGS coverage for one sample in the case"""


class DragenWgsHist(CaseQcForSampleBaseModel):
    """WGS coarse coverage metrics for one sample in the case"""

    #: The histogram keys
    keys = ArrayField(
        models.CharField(max_length=200), null=False, blank=False, max_length=MAX_ARRAY_LENGTH
    )
    # The histogram values
    values = ArrayField(models.FloatField(), null=False, blank=False, max_length=MAX_ARRAY_LENGTH)


class DragenRegionMixin(models.Model):
    """Mixin that adds ``region_name`` to Dragen models"""

    #: The name of the region.
    region_name = models.CharField(max_length=200, null=False, blank=False)

    class Meta:
        abstract = True


class DragenRegionCoverageMetrics(DragenRegionMixin, DragenBaseMetricsForSample):
    """Region based overall coverage."""


class DragenRegionFineHist(DragenRegionMixin, DragenBaseHistogram):
    """Region coarse coverage histogram."""


class DragenRegionHist(DragenRegionMixin, DragenBaseMetricsForSample):
    """Region coarse coverage histogram."""


class DragenRegionOverallMeanCov(DragenRegionMixin, DragenBaseMetricsForSample):
    """Region based overall coverage."""


class BcftoolsStatsSnRecord(pydantic.BaseModel):
    """A Record from the ``SN`` lines in ``bcftools stats`` output."""

    #: Name of the summarized metric
    key: str
    #: Value of the summarized metric
    value: int | float | str | None


class BcftoolsStatsTstvRecord(pydantic.BaseModel):
    """A Record from the ``TSTV`` lines in ``bcftools stats`` output."""

    #: ts
    ts: int
    #: tv
    tv: int
    #: ts/tv
    tstv: float
    #: ts (1st ALT)
    ts_1st_alt: int
    #: tv (1st ALT)
    tv_1st_alt: int
    #: ts/tv (1st ALT)
    tstv_1st_alt: float


class BcftoolsStatsSisRecord(pydantic.BaseModel):
    """A Record from the ``SiS`` (singleton stats) lines in ``bcftools stats`` output."""

    #: allele count
    total: int
    #: number of SNPs
    snps: int
    #: number of transitions (1st ALT)
    ts: int
    #: number of transversions (1st ALT)
    tv: int
    #: number of indels
    indels: int
    #: repeat-consistent
    repeat_consistent: int
    #: repeat-inconsistent
    repeat_inconsistent: int


class BcftoolsStatsAfRecord(pydantic.BaseModel):
    """A Record from the ``AF`` (non-reference allele frequency) lines in ``bcftools stats``
    output."""

    #: allele frequency
    af: float
    #: number of SNPs
    snps: int
    #: number of transitions (1st ALT)
    ts: int
    #: number of transversions (1st ALT)
    tv: int
    #: number of indels
    indels: int
    #: repeat-consistent
    repeat_consistent: int
    #: repeat-inconsistent
    repeat_inconsistent: int
    #: not applicable
    na: int


class BcftoolsStatsQualRecord(pydantic.BaseModel):
    """A Record from the ``QUAL`` (quality) lines in ``bcftools stats`` output."""

    #: quality
    qual: float | None
    #: number of SNPs
    snps: int
    #: number of transitions (1st ALT)
    ts: int
    #: number of transversions (1st ALT)
    tv: int
    #: number of indels
    indels: int


class BcfToolsStatsIddRecord(pydantic.BaseModel):
    """A Record from the ``IDD`` (indel distribution) lines in ``bcftools stats`` output."""

    #: length (deletions negative)
    length: int
    #: number of sites
    sites: int
    #: number of genotypes
    gts: int
    #: mean VAF
    mean_vaf: float | None


class BcftoolsStatsStRecord(pydantic.BaseModel):
    """A Record from the ``ST`` (substitution types) lines in ``bcftools stats`` output."""

    #: type of the substitution
    type: str
    #: count
    count: int


class BcftoolsStatsDpRecord(pydantic.BaseModel):
    """A Record from the ``DP`` (AF) lines in ``bcftools stats`` output."""

    #: bin number
    bin: int
    #: number of genotypes
    gts: int
    #: fraction of genotypes
    gts_frac: float
    #: number of sites
    sites: int
    #: fraction of sites
    sites_frac: float


class BcftoolsStatsMetrics(CaseQcBaseModel):
    """Statistics from ``bcftools stats`` output."""

    #: summary (``SN`` records)
    sn = SchemaField(schema=list[BcftoolsStatsSnRecord], blank=False, null=False)
    #: transition / transversion ratios (``TSTV`` records)
    tstv = SchemaField(schema=list[BcftoolsStatsTstvRecord], blank=False, null=False)
    #: singleton stats (``SiS`` records)
    sis = SchemaField(schema=list[BcftoolsStatsSisRecord], blank=False, null=False)
    #: non-reference allele frequency (``AF`` records)
    af = SchemaField(schema=list[BcftoolsStatsAfRecord], blank=False, null=False)
    #: quality (``QUAL`` records)
    qual = SchemaField(schema=list[BcftoolsStatsQualRecord], blank=False, null=False)
    #: indel distribution
    idd = SchemaField(schema=list[BcfToolsStatsIddRecord], blank=False, null=False)
    #: substitution types
    st = SchemaField(schema=list[BcftoolsStatsStRecord], blank=False, null=False)
    #: depth distribution
    dp = SchemaField(schema=list[BcftoolsStatsDpRecord], blank=False, null=False)


class SamtoolsStatsChkRecord(pydantic.BaseModel):
    """A Record from the ``CHK`` lines in ``samtools stats`` output."""

    #: read names CRC32
    read_names_crc32: str
    #: sequences CRC32
    sequences_crc32: str
    #: qualities CRC32
    qualities_crc32: str


class SamtoolsStatsSnRecord(pydantic.BaseModel):
    """A Record from the ``SN`` lines in ``samtools stats`` output."""

    #: name of the summarized metric
    key: str
    #: value of the summarized metric
    value: int


class SamtoolsStatsFqRecord(pydantic.BaseModel):
    """A Record from the ``FFQ`` and ``LFQ`` lines in ``samtools stats`` output."""

    #: cycle
    cycle: int
    #: counts
    counts: list[int]


class SamtoolsStatsGcRecord(pydantic.BaseModel):
    """A Record from the ``GCF`` and ``GCL`` lines in ``samtools stats`` output."""

    #: GC content
    gc_content: float
    #: count
    count: int


class SamtoolsStatsBasePercentagesRecord(pydantic.BaseModel):
    """A Record from the ``GCC``, ``GCT``, ``FBC``, and ``LBC`` lines in ``samtools stats``
    output.
    """

    #: cycle
    cycle: int
    #: fraction of A, C, G, T
    percentages: list[float]


class SamtoolsStatsIsRecord(pydantic.BaseModel):
    """Records for the ``IS`` records."""

    #: insert size
    insert_size: int
    #: pairs total
    pairs_total: int
    #: inward oriented pairs
    pairs_inward: int
    #: outward oriented pairs
    pairs_outward: int
    #: other pairs
    pairs_other: int


class SamtoolsStatsHistoRecord(pydantic.BaseModel):
    """A record for a value/count pair.

    Used for ``MAPQ``, ``ID``, ``COV``
    """

    #: value
    value: int
    #: count
    count: int


class SamtoolsStatsIdRecord(pydantic.BaseModel):
    """A record for the ``ID`` lines in ``samtools stats`` output."""

    #: length
    length: int
    #: number of insertions
    ins: int
    #: number of deletions
    dels: int


class SamtoolsStatsIcRecord(pydantic.BaseModel):
    """A record for the ``IC`` lines in ``samtools stats`` output."""

    #: cycle
    cycle: int
    #: number of insertions on forward
    ins_fwd: int
    #: number of insertions on reverse
    dels_fwd: int
    #: number of deletions on forward
    ins_rev: int
    #: number of deletions on reverse
    dels_rev: int


class SamtoolsStatsGcdRecord(pydantic.BaseModel):
    """A record for the ``GCD`` lines in ``samtools stats`` output."""

    #: GC content
    gc_content: float
    #: unique sequence percentiles
    unique_seq_percentiles: float
    #: 10th depth percentile
    dp_percentile_10: float
    #: 25th depth percentile
    dp_percentile_25: float
    #: 50th depth percentile
    dp_percentile_50: float
    #: 75th depth percentile
    dp_percentile_75: float
    #: 90th depth percentile
    dp_percentile_90: float


class SamtoolsStatsMainMetrics(CaseQcForSampleBaseModel):
    """Metrics for the most relevant metrics from ``samtools stats`` records.

    This is split between two models so the supplementary data can loaded only when
    necessary.  This split was done with visualization in VarFish in mind.
    """

    #: summary information
    sn = SchemaField(schema=list[SamtoolsStatsSnRecord], blank=False, null=False)
    #: checksum information
    chk = SchemaField(schema=list[SamtoolsStatsChkRecord], blank=False, null=False)
    #: insert size statistics
    isize = SchemaField(schema=list[SamtoolsStatsIsRecord], blank=False, null=False)
    #: coverage distribution
    cov = SchemaField(schema=list[SamtoolsStatsHistoRecord], blank=False, null=False)
    #: GC-depth
    gcd = SchemaField(schema=list[SamtoolsStatsGcdRecord], blank=False, null=False)
    #: first fragment read lengths
    frl = SchemaField(schema=list[SamtoolsStatsHistoRecord], blank=False, null=False)
    #: last fragment read lengths
    lrl = SchemaField(schema=list[SamtoolsStatsHistoRecord], blank=False, null=False)
    #: indel distribution
    idd = SchemaField(schema=list[SamtoolsStatsIdRecord], blank=False, null=False)
    #: first fragment qualities for each cycle
    ffq = SchemaField(schema=list[SamtoolsStatsFqRecord], blank=False, null=False)
    #: last fragment qualities for each cycle
    lfq = SchemaField(schema=list[SamtoolsStatsFqRecord], blank=False, null=False)
    #: first fragment ACGT content for each cycle
    fbc = SchemaField(schema=list[SamtoolsStatsBasePercentagesRecord], blank=False, null=False)
    #: last fragment ACGT content for each cycle
    lbc = SchemaField(schema=list[SamtoolsStatsBasePercentagesRecord], blank=False, null=False)


class SamtoolsStatsSupplementaryMetrics(CaseQcForSampleBaseModel):
    """Metrics for some "supplementary" metrics from ``samtools stats`` records.

    This is split between two models so the supplementary data can loaded only when
    necessary.  This split was done with visualization in VarFish in mind.
    """

    #: first fragment GC content for each cycle
    gcf = SchemaField(schema=list[SamtoolsStatsGcRecord], blank=False, null=False)
    #: last fragment GC content for each cycle
    gcl = SchemaField(schema=list[SamtoolsStatsGcRecord], blank=False, null=False)
    #: ACGT content for each cycle
    gcc = SchemaField(schema=list[SamtoolsStatsBasePercentagesRecord], blank=False, null=False)
    #: ACGT content for each cycle (read-oriented)
    gct = SchemaField(schema=list[SamtoolsStatsBasePercentagesRecord], blank=False, null=False)
    #: read lengths
    rl = SchemaField(schema=list[SamtoolsStatsHistoRecord], blank=False, null=False)
    #: mapping qualities
    mapq = SchemaField(schema=list[SamtoolsStatsHistoRecord], blank=False, null=False)
    #: indel distribution (per cycle)
    ic = SchemaField(schema=list[SamtoolsStatsIcRecord], blank=False, null=False)


class SamtoolsFlagstatRecord(pydantic.BaseModel):
    """A record for the ``flagstat`` lines in ``samtools stats`` output."""

    #: total (QC-passed reads + QC-failed reads)
    total: int = 0
    #: primary
    primary: int = 0
    #: secondary
    secondary: int = 0
    #: supplementary
    supplementary: int = 0
    #: duplicates
    duplicates: int = 0
    #: primary duplicates
    duplicates_primary: int = 0
    #: mapped
    mapped: int = 0
    #: primary mapped
    mapped_primary: int = 0
    #: paired in sequencing
    paired: int = 0
    #: read1
    fragment_first: int = 0
    #: read2
    fragment_last: int = 0
    #: properly paired (98.51% : N/A)
    properly_paired: int = 0
    #: with itself and mate mapped
    with_itself_and_mate_mapped: int = 0
    #: singletons (0.10% : N/A)
    singletons: int = 0
    #: with mate mapped to a different chr
    with_mate_mapped_to_different_chr: int = 0
    #: with mate mapped to a different chr (mapQ>=5)
    with_mate_mapped_to_different_chr_mapq5: int = 0


class SamtoolsFlagstatMetrics(CaseQcForSampleBaseModel):
    """Metrics for ``samtools flagstat`` output."""

    #: statistics for QC pass records
    qc_pass = SchemaField(schema=SamtoolsFlagstatRecord, blank=False, null=False)
    #: statistics for QC fail records
    qc_fail = SchemaField(schema=SamtoolsFlagstatRecord, blank=False, null=False)


class SamtoolsIdxstatsRecord(pydantic.BaseModel):
    """A record for the lines in ``samtools idxstats`` output."""

    #: contig name
    contig_name: str
    #: contig length
    contig_len: int
    #: mapped fragments
    mapped: int
    #: unmapped fragments
    unmapped: int


class SamtoolsIdxstatsMetrics(CaseQcForSampleBaseModel):
    """Metrics for ``samtools idxstats`` output."""

    #: Metrics as JSON following the ``SamtoolsIdxstatsRecord`` schema
    records = SchemaField(schema=list[SamtoolsIdxstatsRecord], blank=False, null=False)


class CraminoSummaryRecord(pydantic.BaseModel):
    """Store a summary record from the cramino output file."""

    #: key
    key: str
    #: value
    value: int | float | str


class CraminoChromNormalizedCountsRecord(pydantic.BaseModel):
    """Store one chrom/normalized read counts record from Cramino output."""

    #: chromosome name
    chrom_name: str
    #: fraction of reads
    normalized_counts: float


class CraminoMetrics(CaseQcForSampleBaseModel):
    """Metrics obtained from cramino."""

    #: summary metric records
    summary = SchemaField(schema=list[CraminoSummaryRecord], blank=False, null=False)
    #: per-chromosome normalized read counts
    chrom_counts = SchemaField(
        schema=list[CraminoChromNormalizedCountsRecord], blank=False, null=False
    )


class NgsbitsMappingqcRecord(pydantic.BaseModel):
    """One entry in the output of ngs-bits' MappingQC."""

    #: key
    key: str
    #: value
    value: int | float | str | None


class NgsbitsMappingqcMetrics(CaseQcForSampleBaseModel):
    """Metrics obtained from ngs-bits' MappingQC."""

    #: the name of the region.
    region_name = models.CharField(max_length=200, null=False, blank=False)
    #: records
    records = SchemaField(schema=list[NgsbitsMappingqcRecord], blank=False, null=False)
